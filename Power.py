#!/usr/bin/env python
import win10toast
import psutil

notifier = win10toast.ToastNotifier()


def reader():
    while True:
        battery = psutil.sensors_battery()
        if battery.percent > 90 and battery.power_plugged:
            notifier.show_toast("Alert", "Battery is above 90")
            break
        elif battery.percent < 25 and not battery.power_plugged:
            notifier.show_toast("Alert", "Battery below 25")
            break
    reader()


reader()
