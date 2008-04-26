
%define plugin	decruft
%define name	vdr-plugin-%plugin
%define version	0.0.4
%define rel	9

Summary:	VDR plugin: Remove the cruft from your channels
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.rst38.org.uk/vdr/decruft/
Source:		http://www.rst38.org.uk/vdr/decruft/vdr-%plugin-%version.tar.bz2
Patch0:		02_avoid-vdr-patch.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Clean the cruft from your channels file - i.e. turn on add channels
without fear of being overwhelmed. Sort your channels into logical
groups.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep
rm -r examples/CVS

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY examples
