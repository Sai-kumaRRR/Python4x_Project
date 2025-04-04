from abc import ABC,abstractmethod


class GearBox(ABC):

    @abstractmethod
    def set_gear(self):
        pass
    class Engine(GearBox):
        @abstractmethod
        def start(self):
            super().set_gear()
            pass

        @abstractmethod
        def stop(self):
            pass

        class Car(engine):
            def start(self):
                print("starting")

                def stop(self):
                    print("stop")

                    def set_gear(self):
                        print("Gearbox is ready")

                        def drive(self):
                            self.start()
                            self.stop()

