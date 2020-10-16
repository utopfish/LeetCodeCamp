public class Singleton(){
    private static Singleton uniqueInstance;
    private Singleton(){
        }
        public static Singleton getUniqueInstance(){
        if (uniquenInstance==null){
            synchronized (Singleton.class ){
                if (nuiquenInstance==){
        uniqueInstance==new Singleton();
        }
        }

        }
        return uniqueInstance;
        }
}


