%define name	powerpc-utils-papr
%define version	0.0.1
%define release %mkrel 2

Summary:	Maintenance utilities for IBM POWER platforms
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	IBM Common Public License
Group:		System/Configuration/Hardware
Url:		https://powerpc-utils.ozlabs.org/
ExclusiveArch:	ppc ppc64
BuildRequires:	librtas-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The powerpc-utils-papr package provides the utilities listed below
which are intended for the maintenance of IBM powerpc platforms that
follow the POWER Architecture Platform Reference.

   * activate_firmware - concurrent firmware activation
   * hvcsadmin - HVCS driver administration utility
   * ibmvscsis.sh - IBMVSCSIS driver init script
   * rtas_dump - dump the contents of a rtas event
   * rtas_event_decode - dump the contents of a rtas event
   * rtas_ibm_get_vpd - gather Vital Product Data that changes dynamically
   * serv_config/uspchrp - configure service processor settings
   * set_poweron_time - configure time for system power-on
   * uesensor - view the state of environental sensors on powerpc machines
   * update_flash - system firmware update utility
   * usysattn, usysfault - attention indicator utility
   * usysident - identification indicator utility
   * vscsisadmin - IBM Virtual SCSI Server (ibmvscsis) administration utilities

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}

%makeinstall_std
rm -rf %{buildroot}%{_datadir}/doc

# XXX check what to actually do with this one
rm -f %{buildroot}%{_sysconfdir}/init.d/ibmvscsis.sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYRIGHT
%{_sbindir}/activate_firmware
%{_sbindir}/hvcsadmin
%{_sbindir}/rtas_dump
%{_sbindir}/rtas_event_decode
%{_sbindir}/rtas_ibm_get_vpd
%{_sbindir}/serv_config
%{_sbindir}/set_poweron_time
%{_sbindir}/uesensor
%{_sbindir}/update_flash
%{_sbindir}/usysattn
%{_sbindir}/usysident
%{_sbindir}/vscsisadmin
%{_mandir}/man8/activate_firmware.8*
%{_mandir}/man8/hvcsadmin.8*
%{_mandir}/man8/ibmvscsis.conf.8*
%{_mandir}/man8/ibmvscsis.sh.8*
%{_mandir}/man8/rtas_dump.8*
%{_mandir}/man8/rtas_ibm_get_vpd.8*
%{_mandir}/man8/serv_config.8*
%{_mandir}/man8/set_poweron_time.8*
%{_mandir}/man8/uesensor.8*
%{_mandir}/man8/update_flash.8*
%{_mandir}/man8/usysattn.8*
%{_mandir}/man8/usysident.8*
%{_mandir}/man8/vscsisadmin.8*

