Summary:	An old-school polyphonic additive synthesizer
Name:		padthv1
Version:	0.9.19
Release:	1
License:	GPLv2+
Group:		Sound/Midi
URL:		https://padthv1.sourceforge.io
Source0:	http://sourceforge.net/projects/padthv1/files/padthv1/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	qt5-qttools
BuildRequires: qt5-qtchooser
BuildRequires:	qt5-linguist
BuildRequires:	qt5-linguist-tools
BuildRequires: qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(lv2)

%description
padthv1 is an old-school polyphonic additive synthesizer with stereo fx.
padthv1 is based on the PADsynth algorithm by Paul Nasca, as a special
variant of additive synthesis.

Features:
  * a pure stand-alone JACK client with JACK-session, NSM (Non Session
    management) and both JACK MIDI and ALSA MIDI input support.
  * a LV2 instrument plug-in.
    URI: http://padthv1.sourceforge.net/lv2

%files
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/%{name}_jack
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/mimetypes/application-x-%{name}-*.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-%{name}-*.svg
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}*.1*
%{_mandir}/fr/man1/padthv1.1.*

#--------------------------------------------------------------------

%define lv2name	lv2-%{name}

%package -n	%{lv2name}
Summary:	Synthesizer LV2 plugin for %{name}
Group:		Sound/Midi
Requires:	%{name} = %{version}

%description -n	%{lv2name}
padthv1 is an old-school polyphonic additive synthesizer with stereo fx.
padthv1 is based on the PADsynth algorithm by Paul Nasca, as a special
variant of additive synthesis.

%files -n %{lv2name}
%{_libdir}/lv2/%{name}.lv2/

#--------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure --enable-debug
%make_build

%install
%make_install

#menu
desktop-file-install \
  --remove-key="X-SuSE-translate" \
  --remove-key="Version" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop
