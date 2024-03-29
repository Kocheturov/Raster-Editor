#include <iostream>
#include "GraphicsFileHandler.h"
#include "Printing.h"
#include "CodeEditor.h"
#include "GIFEditor.h"
#include "CloudIntegration.h"

int main() {
    GraphicsFileHandler fileHandler;
    Printing printer;

    fileHandler.openFile();
    fileHandler.saveFile();
    printer.print();
    
    CodeEditor editor;
    GIFEditor gifEditor;
    CloudIntegration cloudIntegration;

    editor.editFilterCode();
    gifEditor.createGIF();
    cloudIntegration.integrate();

    return 0;
}
