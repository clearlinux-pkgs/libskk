#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD605848ED7E69871 (ueno@gnu.org)
#
Name     : libskk
Version  : 1.0.5
Release  : 1
URL      : https://github.com/ueno/libskk/releases/download/1.0.5/libskk-1.0.5.tar.xz
Source0  : https://github.com/ueno/libskk/releases/download/1.0.5/libskk-1.0.5.tar.xz
Source1 : https://github.com/ueno/libskk/releases/download/1.0.5/libskk-1.0.5.tar.xz.sig
Summary  : a library to deal with Japanese kana-to-kanji conversion method
Group    : Development/Tools
License  : GPL-3.0
Requires: libskk-bin = %{version}-%{release}
Requires: libskk-data = %{version}-%{release}
Requires: libskk-lib = %{version}-%{release}
Requires: libskk-license = %{version}-%{release}
Requires: libskk-locales = %{version}-%{release}
Requires: libskk-man = %{version}-%{release}
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gee-0.8)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : util-linux

%description
libskk -- a library to deal with Japanese kana-to-kanji conversion method
Features:

%package bin
Summary: bin components for the libskk package.
Group: Binaries
Requires: libskk-data = %{version}-%{release}
Requires: libskk-license = %{version}-%{release}

%description bin
bin components for the libskk package.


%package data
Summary: data components for the libskk package.
Group: Data

%description data
data components for the libskk package.


%package dev
Summary: dev components for the libskk package.
Group: Development
Requires: libskk-lib = %{version}-%{release}
Requires: libskk-bin = %{version}-%{release}
Requires: libskk-data = %{version}-%{release}
Provides: libskk-devel = %{version}-%{release}
Requires: libskk = %{version}-%{release}

%description dev
dev components for the libskk package.


%package lib
Summary: lib components for the libskk package.
Group: Libraries
Requires: libskk-data = %{version}-%{release}
Requires: libskk-license = %{version}-%{release}

%description lib
lib components for the libskk package.


%package license
Summary: license components for the libskk package.
Group: Default

%description license
license components for the libskk package.


%package locales
Summary: locales components for the libskk package.
Group: Default

%description locales
locales components for the libskk package.


%package man
Summary: man components for the libskk package.
Group: Default

%description man
man components for the libskk package.


%prep
%setup -q -n libskk-1.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572891706
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1572891706
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libskk
cp %{_builddir}/libskk-1.0.5/COPYING %{buildroot}/usr/share/package-licenses/libskk/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
%find_lang libskk

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/skk

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Skk-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/libskk/rules/README.rules
/usr/share/libskk/rules/act/keymap/default.json
/usr/share/libskk/rules/act/keymap/hankaku-katakana.json
/usr/share/libskk/rules/act/keymap/hiragana.json
/usr/share/libskk/rules/act/keymap/katakana.json
/usr/share/libskk/rules/act/keymap/latin.json
/usr/share/libskk/rules/act/keymap/wide-latin.json
/usr/share/libskk/rules/act/metadata.json
/usr/share/libskk/rules/act/rom-kana/default.json
/usr/share/libskk/rules/act09/keymap/default.json
/usr/share/libskk/rules/act09/keymap/hankaku-katakana.json
/usr/share/libskk/rules/act09/keymap/hiragana.json
/usr/share/libskk/rules/act09/keymap/katakana.json
/usr/share/libskk/rules/act09/keymap/latin.json
/usr/share/libskk/rules/act09/keymap/wide-latin.json
/usr/share/libskk/rules/act09/metadata.json
/usr/share/libskk/rules/act09/rom-kana/default.json
/usr/share/libskk/rules/azik/keymap/common.json
/usr/share/libskk/rules/azik/keymap/default.json
/usr/share/libskk/rules/azik/keymap/hankaku-katakana.json
/usr/share/libskk/rules/azik/keymap/hiragana.json
/usr/share/libskk/rules/azik/keymap/katakana.json
/usr/share/libskk/rules/azik/keymap/latin.json
/usr/share/libskk/rules/azik/keymap/wide-latin.json
/usr/share/libskk/rules/azik/metadata.json
/usr/share/libskk/rules/azik/rom-kana/default.json
/usr/share/libskk/rules/default/keymap/default.json
/usr/share/libskk/rules/default/keymap/hankaku-katakana.json
/usr/share/libskk/rules/default/keymap/hiragana.json
/usr/share/libskk/rules/default/keymap/katakana.json
/usr/share/libskk/rules/default/keymap/latin.json
/usr/share/libskk/rules/default/keymap/wide-latin.json
/usr/share/libskk/rules/default/metadata.json
/usr/share/libskk/rules/default/rom-kana/default.json
/usr/share/libskk/rules/kzik/keymap/common.json
/usr/share/libskk/rules/kzik/keymap/default.json
/usr/share/libskk/rules/kzik/keymap/hankaku-katakana.json
/usr/share/libskk/rules/kzik/keymap/hiragana.json
/usr/share/libskk/rules/kzik/keymap/katakana.json
/usr/share/libskk/rules/kzik/keymap/latin.json
/usr/share/libskk/rules/kzik/keymap/wide-latin.json
/usr/share/libskk/rules/kzik/metadata.json
/usr/share/libskk/rules/kzik/rom-kana/default.json
/usr/share/libskk/rules/nicola/keymap/default.json
/usr/share/libskk/rules/nicola/keymap/hankaku-katakana.json
/usr/share/libskk/rules/nicola/keymap/hiragana.json
/usr/share/libskk/rules/nicola/keymap/kana.json
/usr/share/libskk/rules/nicola/keymap/katakana.json
/usr/share/libskk/rules/nicola/keymap/latin.json
/usr/share/libskk/rules/nicola/keymap/wide-latin.json
/usr/share/libskk/rules/nicola/metadata.json
/usr/share/libskk/rules/nicola/rom-kana/default.json
/usr/share/libskk/rules/tcode/keymap/hankaku-katakana.json
/usr/share/libskk/rules/tcode/keymap/hiragana.json
/usr/share/libskk/rules/tcode/keymap/katakana.json
/usr/share/libskk/rules/tcode/keymap/latin.json
/usr/share/libskk/rules/tcode/keymap/wide-latin.json
/usr/share/libskk/rules/tcode/metadata.json
/usr/share/libskk/rules/tcode/rom-kana/default.json
/usr/share/libskk/rules/trycode/keymap/hankaku-katakana.json
/usr/share/libskk/rules/trycode/keymap/hiragana.json
/usr/share/libskk/rules/trycode/keymap/katakana.json
/usr/share/libskk/rules/trycode/keymap/latin.json
/usr/share/libskk/rules/trycode/keymap/wide-latin.json
/usr/share/libskk/rules/trycode/metadata.json
/usr/share/libskk/rules/trycode/rom-kana/default.json
/usr/share/libskk/rules/tutcode-touch16x/keymap/hankaku-katakana.json
/usr/share/libskk/rules/tutcode-touch16x/keymap/hiragana.json
/usr/share/libskk/rules/tutcode-touch16x/keymap/katakana.json
/usr/share/libskk/rules/tutcode-touch16x/keymap/latin.json
/usr/share/libskk/rules/tutcode-touch16x/keymap/wide-latin.json
/usr/share/libskk/rules/tutcode-touch16x/metadata.json
/usr/share/libskk/rules/tutcode-touch16x/rom-kana/default.json
/usr/share/libskk/rules/tutcode/keymap/hankaku-katakana.json
/usr/share/libskk/rules/tutcode/keymap/hiragana.json
/usr/share/libskk/rules/tutcode/keymap/katakana.json
/usr/share/libskk/rules/tutcode/keymap/latin.json
/usr/share/libskk/rules/tutcode/keymap/wide-latin.json
/usr/share/libskk/rules/tutcode/metadata.json
/usr/share/libskk/rules/tutcode/rom-kana/default.json
/usr/share/vala/vapi/skk-1.0.deps
/usr/share/vala/vapi/skk-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libskk/libskk.h
/usr/lib64/libskk.so
/usr/lib64/pkgconfig/libskk.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libskk.so.0
/usr/lib64/libskk.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libskk/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/skk.1

%files locales -f libskk.lang
%defattr(-,root,root,-)

