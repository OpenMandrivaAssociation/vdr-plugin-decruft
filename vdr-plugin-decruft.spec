%define plugin	decruft

Summary:	VDR plugin: Remove the cruft from your channels
Name:		vdr-plugin-%plugin
Version:	0.0.4
Release:	16
Group:		Video
License:	GPL
URL:		http://www.rst38.org.uk/vdr/decruft/
Source:		http://www.rst38.org.uk/vdr/decruft/vdr-%plugin-%{version}.tgz
Patch0:		02_avoid-vdr-patch.dpatch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Clean the cruft from your channels file - i.e. turn on add channels
without fear of being overwhelmed. Sort your channels into logical
groups.

%prep
%setup -q -n %plugin-%{version}
%patch0 -p1
%vdr_plugin_prep
rm -r examples/CVS

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY examples

