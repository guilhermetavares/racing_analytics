# racing_analytics

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc7e2af47c7c4e41a8354a069179e65a)](https://app.codacy.com/app/zetavares.rib/racing_analytics?utm_source=github.com&utm_medium=referral&utm_content=guilhermetavares/racing_analytics&utm_campaign=Badge_Grade_Dashboard)

This project is the solution for a programing test.
To see all the requirements [link here](https://github.com/Gympass/interview-test/blob/master/README.md)

## Installing

**Important:** This project has developed and idealized using [Docker](https://github.com/Gympass/interview-test/blob/master/README.md) and it is required for the best experience.

## System requirements
* Docker

## Step-by-step

1.  Build the docker, mount the enviroment and prepare for run
```
$ make build
```

2.  For running the project, you need to pass the path of your file like: `path=your/file/path/example.txt`
```
$ make run path=your/file/path/example.txt
```

3.  This project contains unit tests, for see the results, you need to run
```
$ make test
```

4. For see a file example, just run
```
$ make example
```
