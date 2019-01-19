Python I/O redirection with Docker example
===

Toy project experimenting how to use a Python app inside a Docker container to stream commands via STDIN
and receive responses via STDOUT just like you would do with a local Python app.

This might help in deciding how to invoke apps embedded with Docker.

Local invocation
===

Just for reference, this is what I want to achieve:

    $ cat | python3

Toy project experimenting how to use a Python app inside a Docker container to stream commands via STDIN
and receive responses via STDOUT just like you would do with a local Python app.

Local invocation
===

Just for reference, this is what I want to achieve:

    $ cat | python3 my.py 
    1 2 3
    6
    10 20 30
    60
    ^CTraceback (most recent call last):
      File "my.py", line 11, in <module>
          for line in sys.stdin:
          KeyboardInterrupt
          my.py 

Building the Docker image
===

    docker build -t mypy .

Invoking it
===

    $ cat | docker run --rm -i mypy 
    1 2 3
    6
    10 20 30
    60
    ^CTraceback (most recent call last):
      File "my.py", line 12, in <module>
        for line in sys.stdin:
    KeyboardInterrupt

