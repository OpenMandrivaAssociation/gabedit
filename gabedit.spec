%define name	gabedit
%define version	2.0.10
%define tarver	210
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	GUI for comupational chemistry
Version: 	%{version}
Release: 	%{release}

Source:		http://lasim.univ-lyon1.fr/allouche/gabedit/Gabedit%{tarver}Src.tar.gz
Patch:		gabedit_gtk2.12.diff
URL:		http://hplasim2.univ-lyon1.fr/allouche/gabedit
License:	BSD
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	jpeg-devel gtk2-devel libmesaglu-devel

%description
Gabedit is a Graphical User Interface to Gamess-US, Gaussian, Molcas, Molpro
and MPQC computational chemistry packages. Gabedit includes graphical
facilities for generating keywords and options, molecule specifications and
their input sections for even the most advanced calculation types. Gabedit
includes an advanced Molecule Builder. You can use it to rapidly sketch in
molecules and examine them in three dimensions. You can build molecules by
atom, ring, group, amino acid and nucleoside. You can also read geometry from
a file. Most major molecular file formats are supported.

Gabedit includes a Gamess-US, Gaussian, Molcas, Molpro and MPQC Calculation
Setup window which allows you to set up Gamess-US, Gaussian, Molcas, Molpro
and MPQC jobs in a simple and straightforward manner.

Gabedit can graphically display a variety of Gamess-US, Gaussian, Molcas,
Molpro, MPQC and (partially) ADF calculation results, including the following:
- Molecular orbitals
- Surfaces from the electron density, electrostatic potential, NMR shielding
  density, and other properties.
- Surfaces may be displayed in solid, translucent and wire mesh modes. They
  are can be colorcoded by a separate property.
- Contours (colorcoded), Planes colorcoded, Dipole. XYZ axes and the principal
  axes of the molecule.
- Animation of the normal modes corresponding to vibrational frequencies.
- Animation of the rotation of geometry, surfaces, contours, planes colorcoded,
  xyz and the principal axes of the molecule.
- Animation of contours, Animation of planes colorcoded.

Gabedit can display IR and Raman computed spectra.

Gabedit can generate a povray file for geometry (including hydrogen's bond),
surfaces (including colorcoded surfaces), contours, planes colorcoded.

Gabedit can save picture in BMP, JPEG, PNG, PPM and PS format.

Gabedit can generate automatically a series of pictures for animation
(vibration, geometry convergence, rotation, contours, planes colorcoded).

%prep
%setup -q -n Gabedit%{tarver}Src
%patch -p1

%build
%make
										
%install
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=gabedit
Comment=Quantum chemistry interface
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Education;Chemistry;X-MandrivaLinux-MoreApplications-Sciences-Chemistry;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cp icons/Gabedit48.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cp icons/Gabedit32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cp icons/Gabedit16.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc License utils
%{_bindir}/%name
%{_datadir}/applications/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

