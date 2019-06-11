# racing_analytics

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cc7e2af47c7c4e41a8354a069179e65a)](https://app.codacy.com/app/zetavares.rib/racing_analytics?utm_source=github.com&utm_medium=referral&utm_content=guilhermetavares/racing_analytics&utm_campaign=Badge_Grade_Dashboard)

This project is the solution for a developming test, [link here](https://github.com/Gympass/interview-test/blob/master/README.md)

## Step-by-step

1.  Build the docker, mount the enviroment
```
$ make build
```

2.  For running the project, you need to pass the data file like `path=src/example.txt`
```
$ make run path=your/file/path/example.txt
```

3.  This project contains unit tests, for see the results, you need to run
```
$ make test
```
