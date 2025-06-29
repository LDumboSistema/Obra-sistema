import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAr6Q6gR2vs_qDiEc1ESliCAk3y-6kS3-8",
  authDomain: "ldumboapp.firebaseapp.com",
  projectId: "ldumboapp",
  storageBucket: "ldumboapp.firebasestorage.app",
  messagingSenderId: "169934014806",
  appId: "1:169934014806:web:650b5bb94655f9aa032ef7",
  measurementId: "G-J60T6GEM8K"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
export { db };
