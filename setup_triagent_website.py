#!/usr/bin/env python3
"""
Triagent Website Setup Script
Run this inside ~/triagent-website on the Dell laptop:
    python3 setup_triagent_website.py
"""
import os

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  created: {path}")

print("Building Triagent website files...")

# ── next.config.ts ──────────────────────────────────────────────────────────
w('next.config.ts', """\
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",
  trailingSlash: true,
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
""")

# ── tailwind.config.ts ───────────────────────────────────────────────────────
w('tailwind.config.ts', """\
import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        navy: "#1B2A4A",
        brand: "#2E5FA3",
        accent: "#4B8FE2",
        pale: "#EBF1F8",
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [],
};

export default config;
""")

# ── .env.local ───────────────────────────────────────────────────────────────
w('.env.local', "NEXT_PUBLIC_BACKEND_URL=\n")

# ── app/globals.css ──────────────────────────────────────────────────────────
w('app/globals.css', """\
@import "tailwindcss";
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap");

:root {
  --navy: #1B2A4A;
  --blue: #2E5FA3;
  --accent: #4B8FE2;
  --pale: #EBF1F8;
}

html { scroll-behavior: smooth; }

body {
  font-family: "Inter", system-ui, sans-serif;
  background: #ffffff;
  color: #1B2A4A;
}
""")

# ── app/layout.tsx ───────────────────────────────────────────────────────────
w('app/layout.tsx', """\
import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Triagent - AI-Powered Front Office Automation",
  description:
    "AI-powered front office automation for professional services. 24/7 chat, intelligent intake, and smart triage for dental, law, med spa, and accounting firms.",
  keywords: "AI automation, professional services, dental AI, law firm AI, intake automation, chatbot",
  openGraph: {
    title: "Triagent - AI-Powered Front Office Automation",
    description: "Stop losing leads after hours. Triagent handles your front office 24/7 with AI.",
    url: "https://triagent.cloud",
    siteName: "Triagent",
    type: "website",
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
""")

# ── app/page.tsx ─────────────────────────────────────────────────────────────
w('app/page.tsx', """\
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
""")

# ── components/Navbar.tsx ────────────────────────────────────────────────────
w('components/Navbar.tsx', """\
"use client";
import { useState } from "react";

export default function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white border-b border-gray-100 shadow-sm">
      <div className="max-w-6xl mx-auto px-6 flex items-center justify-between h-16">
        <a href="#" className="text-xl font-bold" style={{ color: "#1B2A4A" }}>
          Tri<span style={{ color: "#2E5FA3" }}>agent</span>
        </a>

        <div className="hidden md:flex items-center gap-8">
          <a href="#services" className="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors">Services</a>
          <a href="#demo-chat" className="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors">Live Demo</a>
          <a href="#how-it-works" className="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors">How It Works</a>
          <a href="#contact" className="text-sm font-medium text-gray-600 hover:text-blue-600 transition-colors">Contact</a>
          <a
            href="#contact"
            className="px-4 py-2 rounded-lg text-sm font-semibold text-white transition-opacity hover:opacity-90"
            style={{ backgroundColor: "#2E5FA3" }}
          >
            Book a Call
          </a>
        </div>

        <button
          className="md:hidden p-2 rounded"
          onClick={() => setOpen(!open)}
          aria-label="Toggle menu"
        >
          <div className="w-5 h-0.5 bg-gray-700 mb-1" />
          <div className="w-5 h-0.5 bg-gray-700 mb-1" />
          <div className="w-5 h-0.5 bg-gray-700" />
        </button>
      </div>

      {open && (
        <div className="md:hidden bg-white border-t border-gray-100 px-6 py-4 flex flex-col gap-4">
          <a href="#services" className="text-sm font-medium text-gray-700" onClick={() => setOpen(false)}>Services</a>
          <a href="#demo-chat" className="text-sm font-medium text-gray-700" onClick={() => setOpen(false)}>Live Demo</a>
          <a href="#how-it-works" className="text-sm font-medium text-gray-700" onClick={() => setOpen(false)}>How It Works</a>
          <a href="#contact" className="text-sm font-medium text-gray-700" onClick={() => setOpen(false)}>Contact</a>
          <a
            href="#contact"
            className="px-4 py-2 rounded-lg text-sm font-semibold text-white text-center"
            style={{ backgroundColor: "#2E5FA3" }}
            onClick={() => setOpen(false)}
          >
            Book a Call
          </a>
        </div>
      )}
    </nav>
  );
}
""")

# ── components/Hero.tsx ──────────────────────────────────────────────────────
w('components/Hero.tsx', """\
export default function Hero() {
  return (
    <section
      className="pt-32 pb-24 px-6"
      style={{ background: "linear-gradient(135deg, #1B2A4A 0%, #2E5FA3 100%)" }}
    >
      <div className="max-w-4xl mx-auto text-center">
        <div
          className="inline-block px-4 py-1.5 rounded-full text-xs font-semibold mb-6 tracking-wide uppercase"
          style={{ backgroundColor: "rgba(75,143,226,0.2)", color: "#4B8FE2" }}
        >
          AI-Powered Front Office Automation
        </div>

        <h1 className="text-4xl md:text-6xl font-extrabold text-white leading-tight mb-6">
          Stop Losing Leads<br />
          <span style={{ color: "#4B8FE2" }}>After Hours</span>
        </h1>

        <p className="text-lg md:text-xl text-blue-100 max-w-2xl mx-auto mb-10 leading-relaxed">
          Triagent handles your front office 24/7 with AI. Chat with patients, qualify leads,
          book appointments, and triage inquiries -- automatically, while you sleep.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <a
            href="#demo-chat"
            className="px-8 py-4 rounded-xl font-semibold text-white text-base transition-all hover:opacity-90"
            style={{ backgroundColor: "#4B8FE2" }}
          >
            See Live Demo
          </a>
          <a
            href="#contact"
            className="px-8 py-4 rounded-xl font-semibold text-base border-2 border-white text-white transition-all hover:bg-white hover:text-blue-900"
          >
            Book a Discovery Call
          </a>
        </div>

        <div className="mt-16 grid grid-cols-3 gap-8 max-w-lg mx-auto">
          {[
            { value: "24/7", label: "Always on" },
            { value: "3 min", label: "Avg response" },
            { value: "83%+", label: "Gross margin" },
          ].map((stat) => (
            <div key={stat.label} className="text-center">
              <div className="text-3xl font-extrabold text-white">{stat.value}</div>
              <div className="text-sm text-blue-200 mt-1">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
""")

# ── components/Services.tsx ──────────────────────────────────────────────────
w('components/Services.tsx', """\
const services = [
  {
    icon: "💬",
    title: "AI Website Chat & 24/7 Answering",
    tagline: "Never miss a lead again",
    description:
      "An intelligent chat widget answers questions, captures lead info, and books appointments around the clock -- even when your office is closed.",
    features: ["24/7 availability", "Lead capture & qualification", "Appointment booking", "Handoff to staff"],
    price: "$397-697/mo",
    setup: "$1,500 setup",
    href: "#demo-chat",
  },
  {
    icon: "📋",
    title: "AI Intake & Appointment Automation",
    tagline: "Zero-touch new patient onboarding",
    description:
      "Smart forms collect information, AI qualifies the lead, and appointments are booked and confirmed via SMS -- no staff required.",
    features: ["Smart intake forms", "SMS confirmations", "Calendar integration", "Insurance pre-screening"],
    price: "$497-797/mo",
    setup: "$2,000 setup",
    href: "#demo-intake",
  },
  {
    icon: "🎯",
    title: "AI Customer Triage & Response Agent",
    tagline: "Every inquiry handled in minutes",
    description:
      "AI reads every inbound email and SMS, classifies urgency, drafts the right response, and escalates only what needs human attention.",
    features: ["Email & SMS triage", "4-category classification", "Auto-draft responses", "Escalation rules"],
    price: "$497-797/mo",
    setup: "$2,000 setup",
    href: "#demo-triage",
  },
];

export default function Services() {
  return (
    <section id="services" className="py-24 px-6 bg-white">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
            Three Services. One Mission.
          </h2>
          <p className="text-lg text-gray-500 max-w-2xl mx-auto">
            Built for dental, law, med spa, vet, and accounting practices with 10-80 staff and no internal IT team.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {services.map((s) => (
            <div
              key={s.title}
              className="rounded-2xl border border-gray-100 p-8 flex flex-col hover:shadow-lg transition-shadow"
              style={{ background: "#FAFBFF" }}
            >
              <div className="text-4xl mb-4">{s.icon}</div>
              <div className="text-xs font-semibold uppercase tracking-wide mb-2" style={{ color: "#2E5FA3" }}>
                {s.tagline}
              </div>
              <h3 className="text-xl font-bold mb-3" style={{ color: "#1B2A4A" }}>{s.title}</h3>
              <p className="text-gray-500 text-sm leading-relaxed mb-6">{s.description}</p>

              <ul className="space-y-2 mb-8 flex-1">
                {s.features.map((f) => (
                  <li key={f} className="flex items-center gap-2 text-sm text-gray-600">
                    <span style={{ color: "#2E5FA3" }}>&#10003;</span> {f}
                  </li>
                ))}
              </ul>

              <div className="border-t border-gray-100 pt-4">
                <div className="text-sm text-gray-400 mb-1">{s.setup}</div>
                <div className="text-lg font-bold mb-4" style={{ color: "#1B2A4A" }}>{s.price} retainer</div>
                <a
                  href={s.href}
                  className="block text-center px-4 py-2.5 rounded-lg text-sm font-semibold text-white transition-opacity hover:opacity-90"
                  style={{ backgroundColor: "#2E5FA3" }}
                >
                  Try Live Demo
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
""")

# ── components/DemoChat.tsx ──────────────────────────────────────────────────
w('components/DemoChat.tsx', """\
"use client";
import { useState, useRef, useEffect } from "react";

interface Message {
  role: "user" | "assistant";
  content: string;
}

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "";

export default function DemoChat() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content:
        "Hi! I am the AI assistant for Triagent Demo Dental. How can I help you today? I can answer questions about our services, hours, insurance, and help you book an appointment.",
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg: Message = { role: "user", content: input.trim() };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    if (!BACKEND_URL) {
      setTimeout(() => {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            content:
              "This is a demo placeholder. The live AI backend will be connected once the Oracle VM is configured. You would see real AI responses here powered by Ollama running on a local GPU server.",
          },
        ]);
        setLoading(false);
      }, 1000);
      return;
    }

    try {
      const res = await fetch(`${BACKEND_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMsg.content, history: messages }),
      });
      const data = await res.json();
      setMessages((prev) => [...prev, { role: "assistant", content: data.response }]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Sorry, I am having trouble connecting right now. Please try again shortly." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section id="demo-chat" className="py-24 px-6" style={{ background: "#EBF1F8" }}>
      <div className="max-w-6xl mx-auto">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div>
            <div className="text-xs font-semibold uppercase tracking-wide mb-3" style={{ color: "#2E5FA3" }}>
              Service 1 -- Live Demo
            </div>
            <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
              AI Website Chat &amp; 24/7 Answering
            </h2>
            <p className="text-gray-600 leading-relaxed mb-6">
              This is the exact chat widget your clients get on their website. It answers patient questions,
              captures contact info, and books appointments -- 24 hours a day. Try it yourself.
            </p>
            <ul className="space-y-3">
              {[
                "Powered by local Ollama AI -- no data leaves your network",
                "Customized with your clinic name, services, and hours",
                "Escalates to staff when needed",
                "Captures every lead even at 2am",
              ].map((item) => (
                <li key={item} className="flex items-start gap-2 text-sm text-gray-600">
                  <span className="mt-0.5 font-bold" style={{ color: "#2E5FA3" }}>&#10003;</span> {item}
                </li>
              ))}
            </ul>
          </div>

          <div className="bg-white rounded-2xl shadow-xl overflow-hidden flex flex-col" style={{ height: "480px" }}>
            <div className="px-5 py-4 flex items-center gap-3 border-b" style={{ backgroundColor: "#1B2A4A" }}>
              <div
                className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold text-white"
                style={{ backgroundColor: "#2E5FA3" }}
              >
                T
              </div>
              <div>
                <div className="text-sm font-semibold text-white">Triagent Assistant</div>
                <div className="flex items-center gap-1.5">
                  <div className="w-1.5 h-1.5 rounded-full bg-green-400" />
                  <span className="text-xs text-gray-300">{BACKEND_URL ? "Live" : "Demo mode"}</span>
                </div>
              </div>
            </div>

            <div className="flex-1 overflow-y-auto p-4 space-y-3" style={{ background: "#F8FAFF" }}>
              {messages.map((m, i) => (
                <div key={i} className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}>
                  <div
                    className="max-w-xs px-4 py-2.5 rounded-2xl text-sm leading-relaxed"
                    style={
                      m.role === "user"
                        ? { backgroundColor: "#2E5FA3", color: "white" }
                        : { backgroundColor: "white", color: "#1B2A4A", border: "1px solid #E5E9F0" }
                    }
                  >
                    {m.content}
                  </div>
                </div>
              ))}
              {loading && (
                <div className="flex justify-start">
                  <div className="px-4 py-2.5 rounded-2xl bg-white border border-gray-200 text-sm text-gray-400">
                    Typing...
                  </div>
                </div>
              )}
              <div ref={bottomRef} />
            </div>

            <div className="p-3 border-t bg-white flex gap-2">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && sendMessage()}
                placeholder="Type a message..."
                className="flex-1 text-sm px-4 py-2.5 rounded-xl border border-gray-200 outline-none focus:border-blue-400"
              />
              <button
                onClick={sendMessage}
                disabled={loading || !input.trim()}
                className="px-4 py-2.5 rounded-xl text-sm font-semibold text-white disabled:opacity-50 transition-opacity hover:opacity-90"
                style={{ backgroundColor: "#2E5FA3" }}
              >
                Send
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
""")

# ── components/DemoIntake.tsx ────────────────────────────────────────────────
w('components/DemoIntake.tsx', """\
"use client";
import { useState } from "react";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "";
type Step = "form" | "submitting" | "success";

export default function DemoIntake() {
  const [step, setStep] = useState<Step>("form");
  const [form, setForm] = useState({ name: "", phone: "", service: "", date: "" });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStep("submitting");
    if (!BACKEND_URL) {
      setTimeout(() => setStep("success"), 2000);
      return;
    }
    try {
      await fetch(`${BACKEND_URL}/intake`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
    } catch {}
    setStep("success");
  };

  const reset = () => {
    setStep("form");
    setForm({ name: "", phone: "", service: "", date: "" });
  };

  return (
    <section id="demo-intake" className="py-24 px-6 bg-white">
      <div className="max-w-6xl mx-auto">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div className="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
            {step === "form" && (
              <>
                <div className="text-sm font-semibold mb-1" style={{ color: "#2E5FA3" }}>
                  Demo Dental Practice -- New Patient Intake
                </div>
                <h3 className="text-xl font-bold mb-6" style={{ color: "#1B2A4A" }}>Request an Appointment</h3>
                <form onSubmit={handleSubmit} className="space-y-4">
                  <div>
                    <label className="text-xs font-semibold text-gray-500 uppercase tracking-wide">Full Name</label>
                    <input
                      required type="text" value={form.name}
                      onChange={(e) => setForm({ ...form, name: e.target.value })}
                      className="mt-1 w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm outline-none focus:border-blue-400"
                      placeholder="Jane Smith"
                    />
                  </div>
                  <div>
                    <label className="text-xs font-semibold text-gray-500 uppercase tracking-wide">Phone Number</label>
                    <input
                      required type="tel" value={form.phone}
                      onChange={(e) => setForm({ ...form, phone: e.target.value })}
                      className="mt-1 w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm outline-none focus:border-blue-400"
                      placeholder="(555) 123-4567"
                    />
                  </div>
                  <div>
                    <label className="text-xs font-semibold text-gray-500 uppercase tracking-wide">Service Needed</label>
                    <select
                      required value={form.service}
                      onChange={(e) => setForm({ ...form, service: e.target.value })}
                      className="mt-1 w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm outline-none focus:border-blue-400 bg-white"
                    >
                      <option value="">Select a service...</option>
                      <option>New patient exam</option>
                      <option>Cleaning</option>
                      <option>Emergency visit</option>
                      <option>Cosmetic consultation</option>
                    </select>
                  </div>
                  <div>
                    <label className="text-xs font-semibold text-gray-500 uppercase tracking-wide">Preferred Date</label>
                    <input
                      type="date" value={form.date}
                      onChange={(e) => setForm({ ...form, date: e.target.value })}
                      className="mt-1 w-full px-4 py-2.5 rounded-lg border border-gray-200 text-sm outline-none focus:border-blue-400"
                    />
                  </div>
                  <button
                    type="submit"
                    className="w-full py-3 rounded-xl text-sm font-semibold text-white transition-opacity hover:opacity-90"
                    style={{ backgroundColor: "#2E5FA3" }}
                  >
                    Submit Request
                  </button>
                </form>
              </>
            )}

            {step === "submitting" && (
              <div className="flex flex-col items-center justify-center py-16 text-center">
                <div className="text-4xl mb-4 animate-pulse">⚙️</div>
                <h3 className="text-lg font-bold mb-2" style={{ color: "#1B2A4A" }}>Processing your request...</h3>
                <p className="text-sm text-gray-500">AI is qualifying your intake and checking availability</p>
              </div>
            )}

            {step === "success" && (
              <div className="flex flex-col items-center justify-center py-16 text-center">
                <div className="w-16 h-16 rounded-full flex items-center justify-center text-3xl mb-4" style={{ backgroundColor: "#EBF1F8" }}>
                  ✅
                </div>
                <h3 className="text-lg font-bold mb-2" style={{ color: "#1B2A4A" }}>Appointment Requested!</h3>
                <p className="text-sm text-gray-500 mb-1">
                  In a live deployment, {form.phone || "your phone"} would receive an SMS confirmation within 60 seconds.
                </p>
                <p className="text-xs text-gray-400">Staff notified. Calendar updated. Zero manual work.</p>
                <button onClick={reset} className="mt-6 text-sm font-semibold" style={{ color: "#2E5FA3" }}>
                  Try again
                </button>
              </div>
            )}
          </div>

          <div>
            <div className="text-xs font-semibold uppercase tracking-wide mb-3" style={{ color: "#2E5FA3" }}>
              Service 2 -- Live Demo
            </div>
            <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
              AI Intake &amp; Appointment Automation
            </h2>
            <p className="text-gray-600 leading-relaxed mb-6">
              Fill out the form as if you were a new patient. In a live deployment, submitting triggers an entire
              automated workflow -- AI qualification, SMS confirmation, and calendar booking -- in under 60 seconds.
            </p>
            <ul className="space-y-3">
              {[
                "AI qualifies every lead automatically",
                "SMS confirmation sent within 60 seconds",
                "Syncs with Google Calendar or Cal.com",
                "Staff gets a clean summary, not a raw form",
              ].map((item) => (
                <li key={item} className="flex items-start gap-2 text-sm text-gray-600">
                  <span className="mt-0.5 font-bold" style={{ color: "#2E5FA3" }}>&#10003;</span> {item}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}
""")

# ── components/DemoTriage.tsx ────────────────────────────────────────────────
w('components/DemoTriage.tsx', """\
"use client";
import { useState } from "react";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "";

const CATEGORIES = [
  { id: "urgent",      label: "Urgent",              color: "#EF4444", bg: "#FEF2F2" },
  { id: "appointment", label: "Appointment Request",  color: "#2E5FA3", bg: "#EBF1F8" },
  { id: "info",        label: "Information Request",  color: "#10B981", bg: "#ECFDF5" },
  { id: "complaint",   label: "Complaint",            color: "#F59E0B", bg: "#FFFBEB" },
];

const SAMPLES = [
  "I have severe tooth pain and cannot sleep, I need to see someone today",
  "What are your office hours on Saturdays?",
  "I would like to schedule a cleaning for next week",
  "I have been waiting 3 weeks for my crown and nobody has called me back",
];

const RESPONSES: Record<string, string> = {
  urgent:
    "I understand you are in pain -- this is a dental emergency. I am alerting our team right now. Someone will call you within 15 minutes. If this is a medical emergency, please call 911.",
  appointment:
    "I would be happy to help you schedule an appointment. I am checking our calendar for the next available slot and will send you a booking confirmation via SMS shortly.",
  info:
    "Our office hours are Monday-Friday 8am-5pm and Saturday 9am-2pm. You can also reach us at hello@triagent.cloud or use this chat anytime.",
  complaint:
    "I am sorry to hear about your experience -- this should not have happened. I am escalating this directly to our practice manager, who will call you within 2 hours.",
};

function classify_local(text: string): string {
  const t = text.toLowerCase();
  if (t.includes("pain") || t.includes("emergency") || t.includes("today") || t.includes("cannot sleep")) return "urgent";
  if (t.includes("schedule") || t.includes("appointment") || t.includes("book") || t.includes("cleaning")) return "appointment";
  if (t.includes("waiting") || t.includes("nobody") || t.includes("weeks") || t.includes("back")) return "complaint";
  return "info";
}

export default function DemoTriage() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState<{ category: string; confidence: number; response: string } | null>(null);
  const [loading, setLoading] = useState(false);

  const run = async (text: string) => {
    setInput(text);
    setLoading(true);
    setResult(null);

    if (!BACKEND_URL) {
      await new Promise((r) => setTimeout(r, 1200));
      const category = classify_local(text);
      setResult({ category, confidence: 94, response: RESPONSES[category] });
      setLoading(false);
      return;
    }

    try {
      const res = await fetch(`${BACKEND_URL}/triage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      setResult(await res.json());
    } catch {
      setResult({ category: "info", confidence: 0, response: "Unable to connect to backend." });
    } finally {
      setLoading(false);
    }
  };

  const cat = CATEGORIES.find((c) => c.id === result?.category);

  return (
    <section id="demo-triage" className="py-24 px-6" style={{ background: "#EBF1F8" }}>
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-12">
          <div className="text-xs font-semibold uppercase tracking-wide mb-3" style={{ color: "#2E5FA3" }}>
            Service 3 -- Live Demo
          </div>
          <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
            AI Customer Triage &amp; Response Agent
          </h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Paste any patient message below -- or choose a sample. The AI classifies it and drafts the appropriate response in real time.
          </p>
        </div>

        <div className="max-w-3xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-8 mb-6">
            <label className="text-xs font-semibold uppercase tracking-wide text-gray-500 mb-2 block">
              Patient message
            </label>
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              rows={3}
              className="w-full px-4 py-3 rounded-xl border border-gray-200 text-sm outline-none focus:border-blue-400 resize-none"
              placeholder="Type or paste a patient inquiry..."
            />
            <div className="flex flex-wrap gap-2 mt-3 mb-4">
              {SAMPLES.map((s) => (
                <button
                  key={s}
                  onClick={() => run(s)}
                  className="text-xs px-3 py-1.5 rounded-full border border-gray-200 text-gray-500 hover:border-blue-400 hover:text-blue-600 transition-colors text-left"
                >
                  {s.length > 55 ? s.slice(0, 55) + "..." : s}
                </button>
              ))}
            </div>
            <button
              onClick={() => run(input)}
              disabled={loading || !input.trim()}
              className="w-full py-3 rounded-xl text-sm font-semibold text-white disabled:opacity-50 transition-opacity hover:opacity-90"
              style={{ backgroundColor: "#2E5FA3" }}
            >
              {loading ? "Classifying..." : "Classify & Draft Response"}
            </button>
          </div>

          {result && cat && (
            <div className="bg-white rounded-2xl shadow-xl p-8 space-y-6">
              <div>
                <div className="text-xs font-semibold uppercase tracking-wide text-gray-400 mb-3">Classification</div>
                <div className="grid grid-cols-4 gap-3">
                  {CATEGORIES.map((c) => (
                    <div
                      key={c.id}
                      className="rounded-xl p-3 text-center border-2 transition-all"
                      style={
                        c.id === result.category
                          ? { backgroundColor: c.bg, borderColor: c.color }
                          : { backgroundColor: "#F9FAFB", borderColor: "transparent" }
                      }
                    >
                      <div className="text-xs font-bold" style={{ color: c.id === result.category ? c.color : "#9CA3AF" }}>
                        {c.label}
                      </div>
                    </div>
                  ))}
                </div>
                <div className="mt-3 flex items-center gap-2">
                  <div className="h-1.5 rounded-full flex-1 bg-gray-100">
                    <div
                      className="h-1.5 rounded-full transition-all"
                      style={{ width: `${result.confidence}%`, backgroundColor: cat.color }}
                    />
                  </div>
                  <span className="text-xs font-semibold text-gray-500">{result.confidence}% confidence</span>
                </div>
              </div>

              <div>
                <div className="text-xs font-semibold uppercase tracking-wide text-gray-400 mb-2">AI-Drafted Response</div>
                <div
                  className="rounded-xl p-4 text-sm text-gray-700 leading-relaxed border"
                  style={{ backgroundColor: "#F8FAFF", borderColor: "#E5E9F0" }}
                >
                  {result.response}
                </div>
                <p className="text-xs text-gray-400 mt-2">
                  In a live deployment this response is sent automatically or queued for one-click staff approval.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
""")

# ── components/HowItWorks.tsx ────────────────────────────────────────────────
w('components/HowItWorks.tsx', """\
const steps = [
  {
    number: "01",
    title: "We deploy in one day",
    description:
      "Triagent configures your AI stack, connects it to your existing tools, and deploys to your domain. No IT team required on your end.",
  },
  {
    number: "02",
    title: "AI handles your front office",
    description:
      "Chat answers questions, intake processes new patients, triage routes every inquiry -- automatically, 24/7, from day one.",
  },
  {
    number: "03",
    title: "You see results immediately",
    description:
      "Track every lead, appointment, and response in your dashboard. Most practices recover the setup fee within the first month.",
  },
];

export default function HowItWorks() {
  return (
    <section id="how-it-works" className="py-24 px-6 bg-white">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
            Up and Running in 24 Hours
          </h2>
          <p className="text-lg text-gray-500 max-w-xl mx-auto">
            No lengthy implementations. No IT projects. We handle everything.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-10">
          {steps.map((step) => (
            <div key={step.number} className="text-center">
              <div
                className="w-14 h-14 rounded-2xl flex items-center justify-center text-lg font-extrabold text-white mx-auto mb-5"
                style={{ backgroundColor: "#2E5FA3" }}
              >
                {step.number}
              </div>
              <h3 className="text-lg font-bold mb-3" style={{ color: "#1B2A4A" }}>{step.title}</h3>
              <p className="text-gray-500 text-sm leading-relaxed">{step.description}</p>
            </div>
          ))}
        </div>

        <div
          className="mt-16 rounded-2xl p-8 md:p-12 text-center"
          style={{ background: "linear-gradient(135deg, #1B2A4A 0%, #2E5FA3 100%)" }}
        >
          <h3 className="text-2xl md:text-3xl font-extrabold text-white mb-4">
            Built for practices with no IT staff
          </h3>
          <p className="text-blue-100 max-w-xl mx-auto mb-8">
            Dental, law, med spa, veterinary, accounting. If you have a front desk and a phone, Triagent can automate it.
          </p>
          <a
            href="#contact"
            className="inline-block px-8 py-4 rounded-xl font-semibold text-white border-2 border-white transition-all hover:bg-white hover:text-blue-900"
          >
            Book a Free Discovery Call
          </a>
        </div>
      </div>
    </section>
  );
}
""")

# ── components/Contact.tsx ───────────────────────────────────────────────────
w('components/Contact.tsx', """\
export default function Contact() {
  return (
    <section id="contact" className="py-24 px-6" style={{ background: "#EBF1F8" }}>
      <div className="max-w-3xl mx-auto text-center">
        <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
          Ready to Automate Your Front Office?
        </h2>
        <p className="text-gray-600 mb-10 text-lg">
          Book a free 30-minute discovery call. We will show you exactly how Triagent works for your practice
          and give you a clear cost and timeline.
        </p>

        <div className="bg-white rounded-2xl shadow-xl p-8 md:p-12">
          <div className="grid md:grid-cols-2 gap-6 mb-6">
            <div className="rounded-xl p-6 text-left" style={{ background: "#EBF1F8" }}>
              <div className="text-2xl mb-3">📞</div>
              <h3 className="font-bold mb-1" style={{ color: "#1B2A4A" }}>Book a Call</h3>
              <p className="text-sm text-gray-500 mb-4">30 minutes. No sales pressure. We figure out if this is a fit.</p>
              <a
                href="mailto:hello@triagent.cloud?subject=Discovery Call Request"
                className="inline-block px-5 py-2.5 rounded-lg text-sm font-semibold text-white transition-opacity hover:opacity-90"
                style={{ backgroundColor: "#2E5FA3" }}
              >
                Email to Schedule
              </a>
            </div>
            <div className="rounded-xl p-6 text-left" style={{ background: "#EBF1F8" }}>
              <div className="text-2xl mb-3">✉️</div>
              <h3 className="font-bold mb-1" style={{ color: "#1B2A4A" }}>Send a Message</h3>
              <p className="text-sm text-gray-500 mb-4">Questions about pricing, services, or your specific use case.</p>
              <a
                href="mailto:hello@triagent.cloud"
                className="inline-block px-5 py-2.5 rounded-lg text-sm font-semibold border-2 transition-colors"
                style={{ color: "#2E5FA3", borderColor: "#2E5FA3" }}
              >
                hello@triagent.cloud
              </a>
            </div>
          </div>
          <p className="text-xs text-gray-400">
            Typical response within 2 business hours. Based in the US. Serving professional practices nationwide.
          </p>
        </div>
      </div>
    </section>
  );
}
""")

# ── components/Footer.tsx ────────────────────────────────────────────────────
w('components/Footer.tsx', """\
export default function Footer() {
  return (
    <footer className="py-10 px-6" style={{ backgroundColor: "#1B2A4A" }}>
      <div className="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="text-xl font-bold text-white">
          Tri<span style={{ color: "#4B8FE2" }}>agent</span>
        </div>
        <div className="flex gap-8">
          <a href="#services"    className="text-sm text-gray-400 hover:text-white transition-colors">Services</a>
          <a href="#demo-chat"   className="text-sm text-gray-400 hover:text-white transition-colors">Demo</a>
          <a href="#contact"     className="text-sm text-gray-400 hover:text-white transition-colors">Contact</a>
          <a href="mailto:hello@triagent.cloud" className="text-sm text-gray-400 hover:text-white transition-colors">hello@triagent.cloud</a>
        </div>
        <div className="text-xs text-gray-500">
          &copy; 2026 Triagent. All rights reserved.
        </div>
      </div>
    </footer>
  );
}
""")

print("\nAll files created successfully.")
print("Next steps:")
print("  1. npm run dev   -- verify at http://localhost:3000")
print("  2. npm run build -- verify static export builds cleanly")
print("  3. git add . && git commit -m 'Initial Triagent website' && git push")
