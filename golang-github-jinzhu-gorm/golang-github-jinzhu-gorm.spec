# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/jinzhu/gorm
%global goipath         github.com/jinzhu/gorm
Version:                1.9.16

%gometa

%global goaltipaths     gopkg.in/jinzhu/gorm.v1

%global common_description %{expand:
The fantastic ORM library for Golang, version 1.}

%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        The fantastic ORM library v1 for Golang 

License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/denisenkom/go-mssqldb)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/jinzhu/inflection)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/lib/pq/hstore)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(github.com/jinzhu/now)
%if %{with check}
BuildRequires:  golang(github.com/erikstmartin/go-testdb)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Sep 05 2021 Petr Menšík <pemensik@redhat.com> - 1.9.16-1%{?dist}
- Initial package
