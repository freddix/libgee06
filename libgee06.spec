Summary:	GObject collections library
Name:		libgee06
Version:	0.6.8
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgee/0.6/libgee-%{version}.tar.xz
# Source0-md5:	2688c24f9a12e7616ee808f9092d0afe
URL:		http://live.gnome.org/Libgee
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	vala
Obsoletes:	libgee < 0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgee is a collections library providing GObject-based interfaces and
classes for commonly used data structures.

%package devel
Summary:	Header files for libgee library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgee-devel < 0.7

%description devel
Header files for libgee library.

%prep
%setup -qn libgee-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgee.so.?
%attr(755,root,root) %{_libdir}/libgee.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgee.so
%{_pkgconfigdir}/gee-1.0.pc
%{_includedir}/gee-1.0
%{_datadir}/gir-1.0/Gee-1.0.gir
%{_datadir}/vala/vapi/gee-1.0.vapi

