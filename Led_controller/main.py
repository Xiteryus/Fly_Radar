from code.effects import FillColor

if __name__ == "__main__":
    fill = FillColor(255, 0, 0)  # Rouge plein écran
    if not fill.process():
        fill.print_help()
