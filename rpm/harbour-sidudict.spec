# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-sidudict

# >> macros
%define __provides_exclude_from ^%{_datadir}/.*$
%define __requires_exclude ^libquazip.*$
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    A dictionary program
Version:    0.5
Release:    1
Group:      Qt/Qt
License:    GPLv2+ and dictionaries under cc by-sa 3.0
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-sidudict.yaml
Requires:   mapplauncherd-booster-silica-qt5
Requires:   sailfishsilica-qt5
Requires:   qt5-qtdeclarative-import-xmllistmodel
Requires:   libsailfishapp
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(qdeclarative5-boostable)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sailfishapp)

%description
A dictionary program  based on QStarDict for Stardict dictionaries.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%files
%defattr(0644,root,root,0755)
#%{_datadir}/%{name}/lib
%attr(0755,-,-) /usr/bin/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/qml
#%{_datadir}/%{name}/dic
# >> files
# << files
