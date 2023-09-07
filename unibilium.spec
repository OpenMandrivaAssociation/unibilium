%define major 4
%define oldlibname %mklibname unibilium 0
%define libname %mklibname unibilium
%define devname %mklibname unibilium -d

Name:           unibilium
Version:	2.0.0
Release:        4
Summary:        A terminfo parsing library
License:        LGPL-3.0+
Group:          System/Libraries
Url:            https://github.com/mauke/unibilium/
Source:         https://github.com/mauke/unibilium/archive/v%{version}/unibilium-%{version}.tar.gz
# libtool is a pile of crap that breaks crosscompiling, and
# doesn't serve any valid purpose. Begone!
Patch0:		unibilium-2.0.0-libtool-die-die-die.patch

%description
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

%package -n %{libname}
Summary:        A terminfo parsing library - Shared library package
Group:          System/Libraries
%rename %{oldlibname}

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
%autosetup -p1

%build
%make_build CC="%{__cc}" \
     CFLAGS="%{optflags}" \
     LDFLAGS="%{ldflags}"
     PREFIX="%{_prefix}" \
     LIBDIR="%{_libdir}"

%install
%make_install CFLAGS="%{optflags}" \
     PREFIX="%{_prefix}" \
     LIBDIR="%{_libdir}" \

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%doc GPLv3 LGPLv3 LICENSE
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/unibi*.3*
