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
