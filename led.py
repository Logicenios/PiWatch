# NOT USED
import _rpi_ws281x as ws


# LED configuration.
LED_CHANNEL = 0
LED_COUNT = 1              # How many LEDs to light.
LED_FREQ_HZ = 800000        # Frequency of the LED signal.  Should be 800khz or 400khz.
LED_DMA_NUM = 10            # DMA channel to use, can be 0-14.
LED_GPIO = 18               # GPIO connected to the LED signal line.  Must support PWM!
LED_BRIGHTNESS = 255        # Set to 0 for darkest and 255 for brightest
LED_INVERT = 0              # Set to 1 to invert the LED signal, good if using NPN
#                             transistor as a 3.3V->5V level converter.  Keep at 0
#                             for a normal/non-inverted signal.

LED_STRIP = ws.SK6812_STRIP_RGBW
leds = ws.new_ws2812_t()

channel = ws.ws2811_channel_get(leds, LED_CHANNEL)

ws.ws2811_channel_t_count_set(channel, LED_COUNT)
ws.ws2811_channel_t_gpionum_set(channel, LED_GPIO)
ws.ws2811_channel_t_invert_set(channel, LED_INVERT)
ws.ws2811_channel_t_brightness_set(channel, LED_BRIGHTNESS)
ws.ws2811_channel_t_strip_type_set(channel, LED_STRIP)

ws.ws2811_t_freq_set(leds, LED_FREQ_HZ)
ws.ws2811_t_dmanum_set(leds, LED_DMA_NUM)
