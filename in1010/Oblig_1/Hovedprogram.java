class Hovedprogram {
    public static void main(String[] args) throws Exception {
        Regneklynge abel = new Regneklynge("regneklynge.txt");
        System.out.println("Noder med minst 32 GB: " + abel.noderMedNokMinne(32));
        System.out.prinln("Noder med minst 64 GB: " + abel.noderMedNokMinne(64));
        System.out.prinln("Noder med minst 128 GB: " + abel.noderMedNokMinne(128));
        System.out.prinln("Antall prosessorer: " + abel.antProsessorer());
        System.out.prinln("Antall rack: " + abel.antRacks());
    }
}
