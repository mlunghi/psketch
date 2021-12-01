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

import argparse

def main():
    tf.compat.v1.disable_eager_execution()
    config = configure()
    world = worlds.load(config)
    model = models.load(config)
    trainer = trainers.load(config)
    if config.synonyms is not None:
        trainer.evaluate(model, world)
    else:
        trainer.train(model, world)

def configure():
    # load config
    with open("config.yaml") as config_f:
        config = Struct(**yaml.load(config_f, Loader=yaml.FullLoader))

    parser = argparse.ArgumentParser()
    parser.add_argument("--synonyms")
    args = parser.parse_args()
    if config.synonyms is None and args.synonyms is not None:
        config.synonyms = args.synonyms

    if config.synonyms is not None:
        # set up experiment
        config.experiment_dir = os.path.join("experiments/%s" % config.name)
        assert os.path.exists(config.experiment_dir), \
                "Experiment %s does not exist!" % config.experiment_dir

        # set up logging
        log_name = os.path.join(config.experiment_dir, "{}.log".format(config.synonyms.split("/")[-1]))
        logging.basicConfig(filename=log_name, level=logging.DEBUG,
                format='%(asctime)s %(levelname)-8s %(message)s')
        def handler(type, value, tb):
            logging.exception("Uncaught exception: %s", str(value))
            logging.exception("\n".join(traceback.format_exception(type, value, tb)))
        sys.excepthook = handler

        logging.info("BEGIN")
        logging.info(str(config))
    else:
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
