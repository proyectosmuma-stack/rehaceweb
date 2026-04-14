name: elementor-controls
description: Reference for all standard Elementor widget controls (CONTROL_TYPE::*) used in register_controls(). Covers Text, Number, Select, Color, Media (image/video), Sliders (Dimensions, Border), UI elements (Switcher, Choose, Icon_Select), Data sources (Select2, Query), Typography, and Advanced controls (Gallery, Repeater, URL, Animation). Key fields: label, type, default, options, selectors (CSS mapping with {{VALUE}}), condition/frontend_available, and dynamic (enable/disable dynamic tags).

Usage: $this->add_control( 'id', [ config ] );

1. Basic Controls
TEXT: Controls::TEXT (text inputs)
NUMBER: Controls::NUMBER (min, max, step)
SELECT: Controls::SELECT (options array)
COLOR: Controls::COLOR (alpha support)
SWITCHER: Controls::SWITCHER (label_on, label_off)

2. Media & Visual
MEDIA: Controls::MEDIA (default => [ 'url' => ... ])
GALLERY: Controls::GALLERY
ICONS: Controls::ICONS
SLIDER: Controls::SLIDER (size_units => ['px', 'em', '%', 'rem'])

3. Layout & Styling
DIMENSIONS: Controls::DIMENSIONS (labels => [ 'top', 'right', 'bottom', 'left' ])
BOX_SHADOW: Controls::BOX_SHADOW (selectors)
TEXT_SHADOW: Controls::TEXT_SHADOW (selectors)
BORDER: Group_Control_Border::get_type()
TYPOGRAPHY: Group_Control_Typography::get_type()
BACKGROUND: Group_Control_Background::get_type()

4. Advanced & Selection
SELECT2: Controls::SELECT2 (multiple => true, label_block => true)
REPEATER: Controls::REPEATER (fields array)
URL: Controls::URL (placeholder, show_external, default => [ 'url' => '', 'is_external' => '', 'nofollow' => '' ])
CHOOSE: Controls::CHOOSE (options => [ 'left' => [ 'icon' => 'eicon-text-align-left' ] ])

5. Filters & Logic
Used in \Elementor\Widget_Base::register_controls().
Always include selectors for CSS output:
'selectors' => [
    '{{WRAPPER}} .selector' => 'color: {{VALUE}};',
],

Conditioning:
'condition' => [
    'style_type' => 'custom',
],
