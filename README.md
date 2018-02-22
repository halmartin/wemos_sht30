Micropython script for WeMos D1 with SHT30 temperature/humidity sensor

Reports temperature and humidity to an InfluxDB server at `API`
and database `DB` every `LENGTH` seconds and resets every `LENGTH*60`

Relies on the system time of the InfluxDB server to avoid requiring
NTP support on the WeMos.

Based on the SHT30 module provided by rsc1975/micropython-sht30
