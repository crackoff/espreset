#!/usr/bin/env python
#
# ESP8266 reset script
#
# Copyright (C) 2016 Oleg Krekov

import RPi.GPIO as gpio
import argparse
from time import sleep

def pulldown_pin(pin):
    gpio.setup(pin, gpio.OUT, gpio.PUD_UP)
    gpio.output(pin, False)

parser = argparse.ArgumentParser(description='ESP8266 resetting Utility', prog='espreset')

parser.add_argument(
    '--mode', '-m',
    help='GPIO_MODE := { board | bcm }',
    default='board')

parser.add_argument(
    '--resetpin', '-r',
    help='Raspberry PI pin, which connected to ESP8266 RESET pin',
    required=True,
    type=int)

parser.add_argument(
    '--flashpin', '-f',
    help='Raspberry PI pin, which connected to ESP8266 GPIO0 pin',
    type=int,
    default=-1)

args = parser.parse_args()

if args.mode == 'board':
    gpio.setmode(gpio.BOARD)
elif args.mode == 'bcm':
    gpio.setmode(gpio.BCM)
else:
    raise RuntimeError(args.mode + ' is not a mode')

if args.flashpin != -1:
    pulldown_pin(args.flashpin)
    sleep(0.5)
    print "Flasing mode"

pulldown_pin(args.resetpin)
sleep(0.5)

gpio.cleanup()


