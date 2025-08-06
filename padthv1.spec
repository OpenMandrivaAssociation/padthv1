%global	_enable_debug_packages  %{nil}

Summary:	An old-school polyphonic additive synthesizer
Name:	padthv1
Version:	1.3.2
Release:	1
License:	GPLv2+
Group:	Sound/Midi
Url:		https://padthv1.sourceforge.io
Source0:	http://sourceforge.net/projects/padthv1/files/padthv1/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake >= 3.15
BuildRequires:	desktop-file-utils
BuildRequires:	git
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	cmake(Qt6) >= 6.9
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(fftw3)
BuildRequires: pkgconfig(jack)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(lv2)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(xkbcommon)

%description
This is an old-school polyphonic additive synthesizer with stereo fx. It is
based on the PADsynth algorithm by Paul Nasca, as a special variant
of additive synthesis.
Features:
* a pure stand-alone JACK client with JACK-session, NSM (Non Session
    management) and both JACK MIDI and ALSA MIDI input support.
* A LV2 instrument plug-in.

%files
%doc ChangeLog README
%license LICENSE
%{_bindir}/%{name}_jack
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_datadir}/%{name}/palette/
%{_iconsdir}/hicolor/32x32/apps/org.rncbc.%{name}.png
%{_iconsdir}/hicolor/32x32/mimetypes/org.rncbc.%{name}.application-x-%{name}-preset.png
%{_iconsdir}/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_iconsdir}/hicolor/scalable/mimetypes/org.rncbc.%{name}.application-x-%{name}-preset.svg
%{_datadir}/mime/packages/org.rncbc.%{name}.xml
%{_mandir}/man1/%{name}*.1*
%{_mandir}/fr/man1/%{name}.1.*

#--------------------------------------------------------------------

%define lv2name	lv2-%{name}

%package -n %{lv2name}
Summary:	Synthesizer LV2 plugin for %{name}
Group:	Sound/Midi
Requires:	%{name} = %{version}

%description -n	%{lv2name}
padthv1 is an old-school polyphonic additive synthesizer with stereo fx.
padthv1 is based on the PADsynth algorithm by Paul Nasca, as a special
variant of additive synthesis.

%files -n %{lv2name}
%{_libdir}/lv2/%{name}.lv2/

#--------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake -DCONFIG_QT6=yes \
				-DCONFIG_NSM=no \
				-DCONFIG_WAYLAND=no

%make_build


%install
%make_install -C build

# Fix desktop file
desktop-file-edit \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--add-category="X-OpenMandrivaLinux-CrossDesktop" \
	%{buildroot}%{_datadir}/applications/org.rncbc.padthv1.desktop
