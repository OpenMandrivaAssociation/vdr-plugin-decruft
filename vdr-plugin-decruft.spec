%define plugin	decruft

Summary:	VDR plugin: Remove the cruft from your channels
Name:		vdr-plugin-%plugin
Version:	0.0.4
Release:	14
Group:		Video
License:	GPL
URL:		http://www.rst38.org.uk/vdr/decruft/
Source:		http://www.rst38.org.uk/vdr/decruft/vdr-%plugin-%version.tar.bz2
Patch0:		02_avoid-vdr-patch.dpatch
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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY examples


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4-12mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.4-11mdv2009.1
+ Revision: 359305
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-10mdv2009.0
+ Revision: 197917
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-9mdv2009.0
+ Revision: 197649
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- fix plugin to avoid a vdr patch (P0 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.4-8mdv2008.1
+ Revision: 145060
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-7mdv2008.1
+ Revision: 103082
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-6mdv2008.0
+ Revision: 49987
- rebuild for new vdr

* Fri Jun 22 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-5mdv2008.0
+ Revision: 42705
- rebuild due to buildsystem failure

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-4mdv2008.0
+ Revision: 42074
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-3mdv2008.0
+ Revision: 22802
- rebuild for new vdr

* Sat Apr 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.4-1mdv2008.0
+ Revision: 16575
- initial Mandriva release

