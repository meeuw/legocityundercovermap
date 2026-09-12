#!/usr/bin/python
import fileinput
import json
import functools
import sys

class checkr:
    def __init__(self, f):
        self.f = f
        self.nextline = next(f)
        self.success = True

    def __call__(self, checks, last=False):
        self.line = self.nextline
        if not last:
            self.nextline = next(self.f)
        for fn, err in checks:
            if not fn(self.line):
                self.success = False
                print(f"::error file={self.f.filename()},line={self.f.lineno() - 1}::{err}")


@functools.cache
def get_json(line):
    line = line.strip()
    if line.startswith('"title": '):
        line = line[9:]
    if line.endswith(','):
        line = line[:-1]
    try:
        return json.loads(line)
    except json.decoder.JSONDecodeError:
        return {}

check = checkr(fileinput.input("markers.json"))

check(((lambda line: line == '{\n', "Must start with a single opening curly brace"),))
for typ in (
    "red-brick",
    "alien",
    "silver-statue",
    "cat",
    "boulder",
    "drill-thrill",
    "water-flowers",
    "pig",
    "coffee-break",
    "time-trial",
    "free-run",
    "district-conquered",
    "super-build",
    "super-brick",
    "vehicle-theft",
    "car-jack",
    "gang",
    "atm",
    "train-station",
    "disguise-booth",
    "challenge-entrance",
    "helicopter-platform",
    "crash-mat",
    "fire-extinguished",
    "color-swapper",
    "character-token",
    "vehicle-token",
    "helicopter-token",
    "ferry",
    "call-in-point",
    "police-shield-fragment",
):

    check(((lambda line: line == f'    "{typ}": {{\n', f"Line must be '    \"{typ}\": {{\n'"),))
    check((
        (lambda line: line.startswith('        "title": '), "Line must start with         \"title\": "),
        (lambda line: line.endswith(',\n'), "Line must end with comma"),
        (lambda line: (line[17] == '"' and line[-3] == '"') or (line[17] == '{' and line[-3] == '}'), "title must start and end with \" or { } "),
        (lambda line: isinstance(get_json(line).get('title'), str | None) or get_json(line)['title'].keys() == {'en', 'nl'}, "Must have both en: and nl: titles"),
    ))
    check(((lambda line: line == "        \"markers\": [\n", "Line must be '        \"markers\": ['"),))

    marker_checks = (
        (lambda line: line.startswith('            {"coords": ['), "Line must start with '            {\"coords\": ['"),
        (lambda line: isinstance(get_json(line).get('title'), str | None) or get_json(line)['title'].keys() == {'en', 'nl'}, "Must have both en: and nl: titles"),
        (lambda line: len(get_json(line).keys() - {'coords', 'title', 'tiles', 'description'}) == 0, "Only coords, title, tiles and description keys are supported"),
        (lambda line: len(get_json(line).get('coords', {})) == 2, "Must have exactly two coords"),
    )
    while check.nextline.endswith(',\n'):
        check(
            marker_checks +
            ((lambda line: line.endswith('},\n'), "Line must end with '},'"),),
        )
    check(
        marker_checks +
        ((lambda line: line.endswith('}\n'), "Line must end with '}'"),),
    )

    check(((lambda line: line == '        ]\n', "Must be '        ]'"),))
    if check.nextline == '    }\n':
        break
    check(((lambda line: line == '    },\n', "Must be '    },'"),))
check(((lambda line: line == '    }\n', "Must be '    }'"),))
check(((lambda line: line == '}\n', "Must be '}'"),), True)

if not check.success:
    sys.exit(1)
