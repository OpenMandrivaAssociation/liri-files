%define major 0
%define snapshot 20170221
%define debug_packagr %nil

Summary:        File manager for Liri OS
Name:           liri-files
Version:        0.1.0

%if "%{snapshot}" != ""
# snapshot here
%define tarname %{name}-%{version}-%{snapshot}
Release:        1.%{snapshot}.1
Source0:        %{name}-%{version}-%{snapshot}.tar.xz
%else
# official release here
Release:        1
Source0:	https://github.com/lirios/files/releases/download/v%{version}/%{name}-%{version}.tar.xz
%define tarname %{name}-%{version}
%endif

License:        LGPLv3
Url:            https://github.com/lirios

BuildRequires:  cmake
BuildRequires:	cmake(Fluid)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	pkgconfig(taglib)

%description
File manager for Liri OS

%prep
%setup -qn %{tarname}
%apply_patches

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/%{name}
%{_libdir}/qml/Liri/Files/Archives/libarchivesplugin.so
%{_libdir}/qml/Liri/Files/FolderListModel/libfolderlistmodelplugin.so
%{_libdir}/qml/Liri/Files/PlacesModel/libplacesmodelplugin.so
%{_datadir}/applications/io.liri.Files.desktop
%{_libdir}/qml/Liri/Files/Archives/qmldir
%{_libdir}/qml/Liri/Files/FolderListModel/qmldir
%{_libdir}/qml/Liri/Files/PlacesModel/qmldir
