# Byte Stalker
WIP:Simple port scanner

```
______       _       _____ _        _ _             
| ___ \     | |     /  ___| |      | | |            
| |_/ /_   _| |_ ___\ `--.| |_ __ _| | | _____ _ __ 
| ___ \ | | | __/ _ \`--. \ __/ _` | | |/ / _ \ '__|
| |_/ / |_| | ||  __/\__/ / || (_| | |   <  __/ |   
\____/ \__, |\__\___\____/ \__\____|_|_|\_\___|_|   
        __/ |                                       
       |___/       
```

## Description
```
___  ____ ____ ___    ____ ____ ____ _  _ _  _ ____ ____
|__] |  | |__/  |     [__  |    |__| |\ | |\ | |___ |__/
|    |__| |  \  |     ___] |___ |  | | \| | \| |___ |  \

Port scanner of something host

command: net port-scanner <host> [args]

default: scan ports in range from 1 to 1024

args:
    with port <port> - scan specific port: 'net port-scanner host.com with port 80'
    with ports <...ports> - scan list of ports: 'net port-scanner host.com with ports 80 1 8080 1024'
    in range from <left-limit> to <right-limit> - i think no explanation:
                                                        'net port-scanner host.com in range from 1 to 1024'
```

## How to use
```
  ___      _       ___ _        _ _             _  _ ___ _    ___
 | _ )_  _| |_ ___/ __| |_ __ _| | |_____ _ _  | || | __| |  | _ \
 | _ \ || |  _/ -_)__ \  _/ _` | | / / -_) '_| | __ | _|| |__|  _/
 |___/\_, |\__\___|___/\__\____|_|_\_\___|_|   |_||_|___|____|_|
      |__/

 Short args:
    -h -> get help about program
    -c -> start program with console
 Long args:
    --help -> get help about program
```

## Console help
```
.-. .-. . . .-. .-. .   .-.   . . .-. .   .-.
|   | | |\| `-. | | |   |-    |-| |-  |   |-'
`-' `-' ' ` `-' `-' `-' `-'   ' ` `-' `-' '

prime commands:
    get [args] - get information about something
    help [util] - get help information, also you can use 'get help'
    net [args] - work with network module
    clear - clear screen

get args:
    os - name of os platform
    help - see help in prime commands

net args:
    info - get hostname and ip
    host - get hostname
    ip - get host ip
    port-scanner <host> [args] - ports scanner, about args use 'help port-scanner'

note:
    [...] - optional arg
    <...> - required arg                                                             
```


