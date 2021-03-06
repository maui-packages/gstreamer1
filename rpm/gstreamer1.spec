# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       gstreamer1

# >> macros
# << macros
%define majorminor 1.0

Summary:    GStreamer streaming media framework runtime
Version:    1.4.1
Release:    1
Group:      Applications/Multimedia
License:    LGPLv2+
URL:        http://gstreamer.freedesktop.org/
Source0:    %{name}-%{version}.tar.xz
Source1:    gstreamer1.prov
Source2:    gstreamer1.attr
Source100:  gstreamer1.yaml
Patch0:     gstreamer-inspect-rpm-format.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  check
BuildRequires:  chrpath
BuildRequires:  python
BuildRequires:  gettext-devel

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.


%package devel
Summary:    Development tools for GStreamer
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   glib2-devel >= %{_glib2}
Requires:   libxml2-devel >= %{_libxml2}
Requires:   check-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package tools
Summary:    Common tools and files for GStreamer streaming media framework
Group:      Applications/Multimedia
Requires:   %{name} = %{version}-%{release}

%description tools
This package contains wrapper scripts for the command-line tools that work
with different major/minor versions of GStreamer.


%prep
%setup -q -n %{name}-%{version}/upstream

# gstreamer-inspect-rpm-format.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
export CFLAGS="-DG_DISABLE_ASSERT -DG_DISABLE_CAST_CHECKS"
export NOCONFIGURE="1"
%autogen
# << build pre

%configure --disable-static \
    --with-package-name='Maui GStreamer package' \
    --with-package-origin='http://www.maui-project.org/' \
    --with-buffer-alignment=pagesize \
    --disable-dependency-tracking \
    --disable-examples \
    --disable-tests \
    --disable-valgrind \
    --disable-debug \
    --disable-loadsave \
    --disable-introspection

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# Remove rpath.
chrpath --delete %{buildroot}%{_libdir}/libgstbase-1.0.so.*
chrpath --delete %{buildroot}%{_libdir}/libgstcheck-1.0.so.*
chrpath --delete %{buildroot}%{_libdir}/libgstcontroller-1.0.so.*
chrpath --delete %{buildroot}%{_libdir}/libgstnet-1.0.so.*
chrpath --delete %{buildroot}%{_libdir}/gstreamer-%{majorminor}/libgstcoreelements.so
chrpath --delete %{buildroot}%{_libexecdir}/gstreamer-%{majorminor}/gst-plugin-scanner
chrpath --delete %{buildroot}%{_bindir}/gst-inspect-1.0
chrpath --delete %{buildroot}%{_bindir}/gst-launch-1.0
chrpath --delete %{buildroot}%{_bindir}/gst-typefind-1.0

%find_lang gstreamer-%{majorminor}

# Clean out files that should not be part of the rpm
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

# Add the provides script
install -m0755 -D %{SOURCE1} %{buildroot}%{_rpmconfigdir}/gstreamer1.prov

# Add the gstreamer plugin file attribute entry (rpm >= 4.9.0)
install -m0644 -D %{SOURCE2} %{buildroot}%{_rpmconfigdir}/fileattrs/gstreamer1.attr
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f gstreamer-%{majorminor}.lang
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING NEWS README RELEASE TODO
%{_libdir}/libgstreamer-%{majorminor}.so.*
%{_libdir}/libgstbase-%{majorminor}.so.*
%{_libdir}/libgstcontroller-%{majorminor}.so.*
%{_libdir}/libgstnet-%{majorminor}.so.*
%{_libdir}/libgstcheck-%{majorminor}.so.*
%dir %{_libdir}/gstreamer-%{majorminor}
%{_libdir}/gstreamer-%{majorminor}/libgstcoreelements.so
%dir %{_libexecdir}/gstreamer-%{majorminor}
%{_libexecdir}/gstreamer-%{majorminor}/gst-plugin-scanner
%{_rpmconfigdir}/gstreamer1.prov
%{_rpmconfigdir}/fileattrs/gstreamer1.attr
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%dir %{_includedir}/gstreamer-%{majorminor}
%dir %{_includedir}/gstreamer-%{majorminor}/gst
%{_includedir}/gstreamer-%{majorminor}/gst/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/base
%{_includedir}/gstreamer-%{majorminor}/gst/check
%{_includedir}/gstreamer-%{majorminor}/gst/controller
%{_includedir}/gstreamer-%{majorminor}/gst/net
%{_datadir}/aclocal/gst-element-check-%{majorminor}.m4
%{_libdir}/libgstreamer-%{majorminor}.so
%{_libdir}/libgstbase-%{majorminor}.so
%{_libdir}/libgstcontroller-%{majorminor}.so
%{_libdir}/libgstnet-%{majorminor}.so
%{_libdir}/libgstcheck-%{majorminor}.so
%{_libdir}/pkgconfig/gstreamer-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-base-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-controller-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-check-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-net-%{majorminor}.pc
# << files devel

%files tools
%defattr(-,root,root,-)
# >> files tools
%{_bindir}/gst-inspect-%{majorminor}
%{_bindir}/gst-launch-%{majorminor}
%{_bindir}/gst-typefind-%{majorminor}
%doc %{_mandir}/man1/gst-inspect-%{majorminor}.*
%doc %{_mandir}/man1/gst-launch-%{majorminor}.*
%doc %{_mandir}/man1/gst-typefind-%{majorminor}.*
# << files tools
