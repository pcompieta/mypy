Python I/O redirection with Docker example
===

Toy project experimenting how to use a Python app inside a Docker container to stream commands via STDIN
and receive responses via STDOUT just like you would do with a local Python app.

This might help in deciding how to invoke apps embedded with Docker.

Local invocation (w/o container)
===

Just for reference, this is what I want to achieve:

    $ echo '{"first" : 2, "second" : 3}' | python3 my.py 
    5

Building the Docker image
===

    docker build -t mypy .

Invoking it
===

    $ echo '{"first" : 2, "second" : 3}' | docker run --rm -i mypy 
    5
