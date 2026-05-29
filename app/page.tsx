import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import Services from "@/components/Services";
import DemoChat from "@/components/DemoChat";
import DemoIntake from "@/components/DemoIntake";
import DemoTriage from "@/components/DemoTriage";
import HowItWorks from "@/components/HowItWorks";
import Contact from "@/components/Contact";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <main>
      <Navbar />
      <Hero />
      <Services />
      <DemoChat />
      <DemoIntake />
      <DemoTriage />
      <HowItWorks />
      <Contact />
      <Footer />
    </main>
  );
}
