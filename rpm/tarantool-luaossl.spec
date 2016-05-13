Name: tarantool-luaossl
Version: 1.0.0
Release: 1%{?dist}
Summary: OpenSSL binding for Tarantool
Group: Applications/Databases
License: BSD
URL: https://github.com/tarantool/luaossl
Source0: https://github.com/tarantool/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc >= 4.5
BuildRequires: tarantool-devel >= 1.6.8.0
BuildRequires: openssl-devel
Requires: tarantool >= 1.6.8.0

%description
This package provides an OpenSSL binding library for Tarantool.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir debian
touch debian/changelog
make all5.1

%install
mkdir -p %{buildroot}%{_libdir}/tarantool
cp src/5.1/openssl.so %{buildroot}%{_libdir}/tarantool/_openssl.so
mkdir -p %{buildroot}%{_datarootdir}/tarantool/openssl
cp -r src/*.lua %{buildroot}%{_datarootdir}/tarantool/openssl/

%files
%{_libdir}/tarantool/
%{_datarootdir}/tarantool/*/
%{!?_licensedir:%global license %doc}
%license LICENSE

%changelog
* Fri May 13 2016 Konstantin Nazarov <racktear@tarantool.org> 1.0.0-1
- Initial version of the RPM spec

