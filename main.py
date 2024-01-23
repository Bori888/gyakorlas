import osszegzes
# import eldontes
# import szamitogep_program_metodus
import fajlba_irassal

# print(osszegzes.osszegzo())
# eldontes.szamitas()

# szamitogepek = szamitogep_program_metodus.paldanyositas()
# szamitogep_program_metodus.kiiras(szamitogepek)
# szamitogep_program_metodus.osszegzes_tetele(szamitogepek)
# szamitogep_program_metodus.maximum_kivalaszt(szamitogepek)
# szamitogep_program_metodus.megszamlalas_tetel(szamitogepek)
# szamitogep_program_metodus.eldontes_tetel(szamitogepek)
#


szamitogepek = fajlba_irassal.paldanyositas()
fajlba_irassal.kiiras(szamitogepek)
fajlba_irassal.osszegzes_tetele(szamitogepek)
fajlba_irassal.maximum_kivalaszt(szamitogepek)
fajlba_irassal.megszamlalas_tetel(szamitogepek)
fajlba_irassal.eldontes_tetel(szamitogepek)
