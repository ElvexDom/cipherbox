import logging

class Logger:
    logging.basicConfig(
        filename="app.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    @staticmethod
    def log(level: str, msg, *args, **kwargs):
        """
        Log un message avec le niveau indiqué.

        :param level: Niveau du log ('debug', 'info', 'warning', 'error', 'critical', 'exception')
        :param msg: Message à logger
        """
        func = getattr(logging, level.lower(), logging.info)
        func(msg, *args, **kwargs)
