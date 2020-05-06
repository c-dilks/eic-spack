# [Spack](https://github.com/LLNL/spack) package repo for HEP software packaging

This holds a set of Spack packages for common HEP software.  It relies
on Spack and the builtin Spack packages, some of which are overridden
by this repo.

## Getting started

Initial setup like:

```bash
cd /path/to/big/disk
git clone https://github.com/LLNL/spack.git
cd spack/var/spack/repos
git clone https://github.com/HEP-SF/hep-spack.git
cd -
./spack/bin/spack compiler add /usr/bin/gcc
./spack/bin/spack repo add spack/var/spack/repos/hep-spack
```

To not have to type a full path to `spack` and to gain some other shell-level features do

```bash
$ source spack/share/spack/setup-env.sh
```

This is assumed below.


## Some Exercises

### Install ROOT

```bash
$ spack info root
$ spack install root
```

### Setup environment

If you have [Environment Modules](http://modules.sf.net) installed:

```bash
$ spack load root
$ root
   --------------------------------------------------------------------------
  | Welcome to ROOT 6.07/02                              http://root.cern.ch |
  |                                             (c) 1995-2014, The ROOT Team |
  | Built for linuxx8664gcc                                                  |
  | From heads/master@v6-07-01-ROOTaaS-1-123-gb5924cd, Dec 18 2015, 11:21:36 |
  | Try '.help', '.demo', '.license', '.credits', '.quit'/'.q'               |
   --------------------------------------------------------------------------
```


### Create Geant4 packaging


```bash
$ spack create -r /path/to/big/disk/hep-spack -N hsf -n geant4 http://geant4.cern.ch/support/source/geant4.10.01.p03.tar.gz
```

Your `$EDITOR` will open.  Close the file to continue.  Later, you
locate the file manually or do:

```bash
$ spack edit geant4
$ spack install geant4
```

This fails first time failing to download Xerces-C:

```bash
$ spack versions xerces-c
==> Safe versions (already checksummed):
  3.1.2
==> Remote versions (not yet checksummed):
  256  5  3.1.3  1  c
$ spack checksum xerces-c@3.1.3
...
How many would you like to checksum? (default is 5, q to abort) 3
...
      version('3.1.3', '70320ab0e3269e47d978a6ca0c0e1e2d')
$ spack edit xerces-c
```

Paste that `version` line into the `xerces-c` package.

```bash
$ spack install geant4
...
==> Successfully installed geant4.
  Fetch: 0.00s.  Build: 11m 51.38s.  Total: 11m 51.38s.
```

Now this picks up the newer Xerces-C 3.1.3, builds it and starts
building Geant4.
