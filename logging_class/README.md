# logging module
Generate log message and log file in other python programs

## Version
**v1.2.0**
- Ability to set log file rotate frequency
    - month (default)
    - day

## Usage
**Params**
- `name`: set the logging file name
- `directory`: set logging file placement (Optional)
- `frequency`: set logging file rotate frequency (Optional)

```
PersonalLog(name, [directory='LOG_PATH'], [frequency=month|day])

PersonalLog.debug(message)
PersonalLog.info(message)
PersonalLog.warning(message)
PersonalLog.error(message)
PersonalLog.critical(message)
```