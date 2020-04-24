# -*- coding: utf-8 -*-

"""
@Author             : Bao
@Date               : 2020/4/24 17:00
@Desc               : 
@Last modified by   : Bao
@Last modified date : 2020/4/24 17:00
"""

import logging

logger = logging.getLogger(__name__)


def run(inputs, history):
    history.append(inputs)
    logger.info(history)

    outputs = [(inputs, 0.0)] * 5

    return outputs, history
