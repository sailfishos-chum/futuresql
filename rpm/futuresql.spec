%global qt6_build_dir release-qt6
%global _description %{expand:
FutureSQL was in part inspired by Diesel, and provides a higher level of
abstraction than QtSql. Its features include non-blocking database access by
default, relatively boilerplate-free queries, automatic database migrations
and simple mapping to objects.  In order to make FutureSQL's use of templates
less confusing, FutureSQL uses C++20 concepts, and requires a C++20 compiler.}

Name:    futuresql
Version: 0.1.1
Release: 0%{?dist}
License: (LGPL-2.1-only OR LGPL-3.0-only) AND BSD-2-Clause
Summary: Non-blocking database framework for Qt
URL:     https://invent.kde.org/libraries/futuresql/
Source0: %{name}-%{version}.tar.bz2

BuildRequires: kf6-extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: ninja
BuildRequires: qt6-qtbase-devel
BuildRequires: qcoro-qt6-devel

%description %_description

%package qt6
Summary: Non-blocking database framework for Qt 6

%package qt6-devel
Summary: Development files for FutureSQL (Qt 6 version)
Requires: %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qcoro-qt6-devel

%description qt6 %_description
%description qt6-devel %_description



%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
mkdir -p %{qt6_build_dir}
pushd %{qt6_build_dir}
%cmake -G Ninja \
    -S .. \
    -DBUILD_WITH_QT6:BOOL=ON \
    -DBUILD_EXAMPLES:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON
%cmake_build
popd

%install
pushd %{qt6_build_dir}
%cmake_install
popd

%check
pushd %{qt6_build_dir}
%ctest --timeout 3600
popd

%files qt6
%doc README.md
%license LICENSES/*
%{_libdir}/libfuturesql6.so.0*

%files qt6-devel
%{_includedir}/FutureSQL6/
%{_libdir}/cmake/FutureSQL6/
%{_libdir}/libfuturesql6.so
