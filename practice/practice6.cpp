#include <windows.h>
#include <windows.h>
SetConsoleCP(65001); // кодова сторінка для UTF-8
SetConsoleOutputCP(65001);

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    static HWND hListBox;

    switch (msg) {
    case WM_CREATE:
        hListBox = CreateWindow(
            "LISTBOX",
            NULL,
            WS_CHILD | WS_VISIBLE | WS_VSCROLL | LBS_NOTIFY,
            0, 0, 0, 0,
            hwnd,
            (HMENU)1,
            (HINSTANCE)GetWindowLongPtr(hwnd, GWLP_HINSTANCE),
            NULL);

        SendMessage(hListBox, LB_ADDSTRING, 0, (LPARAM)"First line");
        SendMessage(hListBox, LB_ADDSTRING, 0, (LPARAM)"Second line");
        SendMessage(hListBox, LB_ADDSTRING, 0, (LPARAM)"Third line");
        break;

    case WM_SIZE:
        MoveWindow(hListBox, 0, 0, LOWORD(lParam), HIWORD(lParam), TRUE);
        break;

    case WM_DESTROY:
        PostQuitMessage(0);
        break;

    default:
        return DefWindowProc(hwnd, msg, wParam, lParam);
    }
    return 0;
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    const char g_szClassName[] = "MyWindowClass";

    WNDCLASSEX wc = {0};
    wc.cbSize        = sizeof(WNDCLASSEX);
    wc.style         = CS_HREDRAW | CS_VREDRAW;
    wc.lpfnWndProc   = WndProc;
    wc.hInstance     = hInstance;
    wc.hCursor       = LoadCursor(NULL, IDC_ARROW);
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW+1);
    wc.lpszClassName = g_szClassName;

    RegisterClassEx(&wc);

    HWND hwnd = CreateWindowEx(
        0,
        g_szClassName,
        "ListBox приклад (WinAPI)",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, 400, 300,
        NULL, NULL, hInstance, NULL);

    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0) > 0) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return msg.wParam;
}
