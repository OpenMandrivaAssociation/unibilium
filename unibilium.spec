%define major 0
%define libname %mklibname unibilium %{major}
%define devname %mklibname unibilium -d

Name:           unibilium
Version:        1.2.1
Release:        2
Summary:        A terminfo parsing library
License:        LGPL-3.0+
Group:          System/Libraries
Url:            https://github.com/mauke/unibilium/
Source:         https://github.com/mauke/unibilium/archive/v%{version}/unibilium-%{version}.tar.gz
BuildRequires:  libtool

%description
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

%package -n %{libname}
Summary:        A terminfo parsing library - Shared library package
Group:          System/Libraries

%description -n %{libname}
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

This package holds the shared library.

%package -n	%{devname}
Summary:        A terminfo parsing library - Development files
Group:          Development/C
Requires:       %{libname} = %{EVRD}

%description -n %{devname}
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

This package holds the development files.

%prep
%setup -q

%build
%make CC=%{__cc} \
     CFLAGS="%{optflags}" \
     LDFLAGS="%{ldflags}"
     PREFIX="%{_prefix}" \
     LIBDIR="%{_libdir}"

%install
%make CFLAGS="%{optflags}" \
     PREFIX="%{_prefix}" \
     LIBDIR="%{_libdir}" \
     DESTDIR=%{buildroot} \
     install

%files -n %{libname}
%{_libdir}/lib%{name}.so.*

%files -n %{devname}
%doc GPLv3 LGPLv3 LICENSE
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/unibi*.3*
