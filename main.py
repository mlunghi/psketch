#!/usr/bin/env python2

from misc.util import Struct
import models
import trainers
import worlds

import logging
import numpy as np
import os
import random
import sys
import tensorflow as tf
import traceback
import yaml

import shutil

def main():
    print("A")
    config = configure()
    print("B")
    world = worlds.load(config)
    print("C")
    model = models.load(config)
    print("D")
    trainer = trainers.load(config)
    print("E")
    trainer.train(model, world)
    print("F")

def configure():
    # load config
    with open("config.yaml") as config_f:
        config = Struct(**yaml.load(config_f, Loader=yaml.FullLoader))

    # set up experiment
    config.experiment_dir = os.path.join("experiments/%s" % config.name)
    if os.path.exists(config.experiment_dir):
        shutil.rmtree(config.experiment_dir)
    assert not os.path.exists(config.experiment_dir), \
            "Experiment %s already exists!" % config.experiment_dir
    os.mkdir(config.experiment_dir)

    # set up logging
    log_name = os.path.join(config.experiment_dir, "run.log")
    logging.basicConfig(filename=log_name, level=logging.DEBUG,
            format='%(asctime)s %(levelname)-8s %(message)s')
    def handler(type, value, tb):
        logging.exception("Uncaught exception: %s", str(value))
        logging.exception("\n".join(traceback.format_exception(type, value, tb)))
    sys.excepthook = handler

    logging.info("BEGIN")
    logging.info(str(config))

    return config

if __name__ == "__main__":
    main()
