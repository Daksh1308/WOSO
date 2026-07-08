import simpy
from src.config import SimulationConfig

class WorkerPool:
    def __init__(self, env: simpy.Environment, config: SimulationConfig):
        self.env = env
        self.config = config
        self.resource = simpy.Resource(env, capacity=config.num_workers)
        self.total_workers = config.num_workers
        self._util_samples = []
        self._monitor_process = env.process(self._monitor_utilization())

        num_profiles = len(config.worker_profiles)
        self._walking_speeds = [
            config.worker_profiles[i % num_profiles].walking_speed
            for i in range(config.num_workers)
        ]
        self._next_worker_idx = 0

        self._break_process = env.process(self._manage_breaks())

    def _manage_breaks(self):
        for day in range(self.config.simulation_days):
            for shift in self.config.shifts:
                if shift.break_start is None:
                    continue
                day_offset = day * 24 * 60
                shift_start = day_offset + shift.start_hour * 60
                break_start = shift_start + shift.break_start * 60
                break_end = break_start + shift.break_duration * 60

                wait_until_break = break_start - self.env.now
                if wait_until_break > 0:
                    yield self.env.timeout(wait_until_break)

                requests = [self.resource.request() for _ in range(self.total_workers)]
                for req in requests:
                    yield req

                yield self.env.timeout(break_end - self.env.now)

                for req in requests:
                    self.resource.release(req)

    def _monitor_utilization(self):
        while True:
            self._util_samples.append((self.env.now, self.resource.count))
            yield self.env.timeout(1.0)

    def request(self):
        return self.resource.request()

    def get_next_worker_speed(self) -> float:
        speed = self._walking_speeds[self._next_worker_idx % self.total_workers]
        self._next_worker_idx += 1
        return speed

    def get_utilization(self, current_time: float) -> float:
        if current_time == 0 or not self._util_samples:
            return 0.0
        samples = [s for s in self._util_samples if s[0] <= current_time]
        if not samples:
            return 0.0
        total_busy = sum(count for _, count in samples)
        total_possible = len(samples) * self.total_workers
        return (total_busy / total_possible) * 100 if total_possible > 0 else 0.0

    @property
    def available_workers(self) -> int:
        return self.total_workers - self.resource.count

    @property
    def busy_workers(self) -> int:
        return self.resource.count
