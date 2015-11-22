#!/bin/bash

gid=$(stat --format %g /usr/src/app)
uid=$(stat --format %u /usr/src/app)

groupadd --gid $gid foo
useradd --gid $gid --uid $uid foo

# TODO(andre): usar o gosu
su $(id --user --name $uid) -c "$*"
