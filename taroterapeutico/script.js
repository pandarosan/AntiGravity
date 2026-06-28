document.addEventListener('DOMContentLoaded', () => {
  // ---------------------------------------------------------------------
  // 1. SELECTORS
  // ---------------------------------------------------------------------
  const themeToggle = document.getElementById('theme-toggle');
  const header = document.getElementById('header');
  const mobileNavToggle = document.getElementById('mobile-nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');
  const faqItems = document.querySelectorAll('.faq-item');
  const alcateiaItems = document.querySelectorAll('.alcateia-item');
  const contactForm = document.getElementById('contact-form');
  const backToTop = document.getElementById('back-to-top');
  const copyrightYear = document.getElementById('copyright-year');
  const animatedElements = document.querySelectorAll('.section-header, .hero-content, .hero-media, .therapy-content, .therapy-areas, .specialty-card, .pricing-card, .pricing-single-box, .bio-media, .bio-content, .lobos-box, .faq-item, .alcateia-item, .contact-info, .contact-card');

  // ---------------------------------------------------------------------
  // 2. THEME SWITCHER (DARK / LIGHT)
  // ---------------------------------------------------------------------
  // Check local storage or system preference
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
  }

  themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  });

  // ---------------------------------------------------------------------
  // 3. SCROLL EFFECTS (HEADER & ACTIVE LINKS)
  // ---------------------------------------------------------------------
  window.addEventListener('scroll', () => {
    // Header shadow/glass on scroll
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    // Back to Top button visibility
    if (backToTop) {
      if (window.scrollY > 400) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    }

    // Active nav link highlight on scroll
    let current = '';
    const sections = document.querySelectorAll('section, header.hero');
    const scrollPosition = window.scrollY + 120; // offset

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

  // ---------------------------------------------------------------------
  // 4. MOBILE NAVIGATION MENU
  // ---------------------------------------------------------------------
  mobileNavToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    // Change menu icon representation
    const isOpen = navMenu.classList.contains('active');
    mobileNavToggle.innerHTML = isOpen 
      ? `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`
      : `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>`;
  });

  // Close mobile menu when clicking a link
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('active');
      mobileNavToggle.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>`;
    });
  });

  // ---------------------------------------------------------------------
  // 5. ACCORDION FAQ
  // ---------------------------------------------------------------------
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');
    
    question.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      
      // Close all other items
      faqItems.forEach(otherItem => {
        otherItem.classList.remove('active');
        otherItem.querySelector('.faq-answer').style.maxHeight = null;
      });

      // Toggle current item
      if (!isActive) {
        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  // ---------------------------------------------------------------------
  // 5b. ACCORDION ALCATEIAS
  // ---------------------------------------------------------------------
  alcateiaItems.forEach(item => {
    const header = item.querySelector('.alcateia-header');
    const content = item.querySelector('.alcateia-content');
    
    header.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      
      // Close all other items
      alcateiaItems.forEach(otherItem => {
        otherItem.classList.remove('active');
        otherItem.querySelector('.alcateia-content').style.maxHeight = null;
      });

      // Toggle current item
      if (!isActive) {
        item.classList.add('active');
        content.style.maxHeight = content.scrollHeight + 'px';
      }
    });
  });

  // ---------------------------------------------------------------------
  // 6. ENTRANCE ANIMATIONS (INTERSECTION OBSERVER)
  // ---------------------------------------------------------------------
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const animationObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target); // trigger animation only once
      }
    });
  }, observerOptions);

  animatedElements.forEach(el => {
    animationObserver.observe(el);
  });

  // ---------------------------------------------------------------------
  // 7. CONTACT FORM TO WHATSAPP INTEGRATION
  // ---------------------------------------------------------------------
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const nome = document.getElementById('form-name').value.trim();
      const email = document.getElementById('form-email').value.trim();
      const servico = document.getElementById('form-service').value;
      const mensagem = document.getElementById('form-message').value.trim();
      
      if (!nome || !email || !mensagem) {
        alert('Por favor, preencha todos os campos obrigatórios.');
        return;
      }
      
      // WhatsApp configuration
      const phoneNumber = '5511998834347'; // (11) 99883-4347
      
      let text = `Olá Rosangela! Vi seu site e gostaria de entrar em contato.\n\n`;
      text += `*Nome:* ${nome}\n`;
      text += `*E-mail:* ${email}\n`;
      text += `*Assunto:* ${servico}\n`;
      text += `*Mensagem:* ${mensagem}`;
      
      const encodedText = encodeURIComponent(text);
      const whatsappUrl = `https://api.whatsapp.com/send?phone=${phoneNumber}&text=${encodedText}`;
      
      // Open in a new tab
      window.open(whatsappUrl, '_blank');
      
      // Reset form
      contactForm.reset();
    });
  }

  // ---------------------------------------------------------------------
  // 8. BACK TO TOP CLICK & DYNAMIC COPYRIGHT YEAR
  // ---------------------------------------------------------------------
  if (backToTop) {
    backToTop.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  if (copyrightYear) {
    copyrightYear.textContent = new Date().getFullYear();
  }
});
