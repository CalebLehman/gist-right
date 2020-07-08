# Gist Right

The source code for the `gist` command, which allows the user to
* setup and create a gist (one *global* gist is managed at a time, until
  it is pushed)
* view and clone their gists

Kinda like `git`, but simpler, less robust, and for gists. Created as
an alternative for https://github.com/defunkt/gist because ~it is
better in some way~ (**TODO** come up with a reason for this project's
existence).

Only tested with Python 3.7 on Linux.

# Usage

The `gist` commands are inspired by some of the standard `git`
commands. The intended usage is
* Add and remove files from a single *global* gist
* Push the current *global* gist
* Make and push a single, simple gist (without interfering with the
  current *global* gist)
* View and clone existing gists (at which point, standard Git commands
  can be used)

## `gist quick filename [-d|--description description] [-p|--public]`

Adds `stdin` as a file with name `filename` to a new gist and pushes it.
Does not affect the current *global* gist.

## `gist status`

Display the files in the current global gist.

## `gist mk filename`

Adds `stdin` to the current global gist with name `filename`.

## `gist add [file...]`

Adds a number of files to the current global gist.

## `gist rm [file...]`

Removes a number of files from the current global gist.

## `gist new [-f|--force]`

Clears the current global gist.

## `gist push [-d|--description description] [-p|--public]`

Pushes the current global gist.

## `gist ls`

Lists all gists (id and description).

## `gist show id`

Shows the gist corresponding to `id`.

## `gist clone id path`

Clones the gist corresponding to `id` into the directory given by
`path`. Note that `path` must not be an existing directory and, unlike
the similar `git` command, `path` MUST be specified.

# Security Note

For simplicity, this project assumes you have a [Personal Access
Token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).
The first time you use any of the `gist` commands you will be prompted
for the token, which will be stored at
`$HOME/.config/gistright/gist_token` with owner-only read-write
permissions (similar level of security as your private ssh key, I
think).
