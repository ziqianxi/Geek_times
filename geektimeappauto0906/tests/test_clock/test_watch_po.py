from time import sleep

from clock.page.main_page import MainPage


class TestClock:
    def setup_class(self):
        # app启动并进入默认的clock页面
        self.watch = MainPage().to_watch()

    def teardown_class(self):
        self.watch.quit()
    def setup(self):
        ...

    def test_watch(self):
        old = self.watch.get_total_time()
        self.watch.start()
        sleep(1)
        self.watch.pause()
        assert self.watch.get_total_time() - old > 1

        self.watch.reset()
        assert self.watch.get_total_time() == old

    def test_lap(self):
        self.watch.start()
        for i in range(3):
            sleep(0.5)
            self.watch.lap()
        assert len(self.watch.get_lap_list()) == 3
