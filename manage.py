#!/usr/bin/env python
import os
import sys

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(filename=".env"))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
