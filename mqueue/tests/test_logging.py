import logging
from unittest.mock import patch
from django.test import TestCase
from .base import MqueueBaseTest
from mqueue.models import MEvent


class MqueueTestLogging(MqueueBaseTest):

    """

    # TOFIX

    @patch('mqueue.logging.DEV_LOGGING')
    def test_mqueue_logging(self, mock_logging):
        from mqueue.logging import DEV_LOGGING, LOGGING_WARNING
        logger = logging.getLogger('mqueue.logging.DEV_LOGGING')
        logger.debug('debug logged')
        logger.info('info logged')
        logger.warning('warning logged')
        logger.critical('critical logged')
        self.assertTrue(mock_logging.warn.called)"""
