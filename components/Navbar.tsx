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
